"""Token-usage metadata for generated graphify runbooks.

The numeric token fields remain backwards compatible and contain known totals.
This module carries the separate completeness signal needed to distinguish a
real zero from a host that did not expose usage metrics.
"""
from __future__ import annotations

from datetime import datetime, timezone
from typing import Iterable, Literal, Mapping

TokenUsageStatus = Literal[
    "complete",
    "partial",
    "unavailable",
    "not-used",
    "legacy",
]

_VALID_STATUSES = {
    "complete",
    "partial",
    "unavailable",
    "not-used",
    "legacy",
}


def token_usage(
    status: TokenUsageStatus,
    *,
    tracked_chunks: int = 0,
    untracked_chunks: int = 0,
) -> dict:
    """Build validated, JSON-serializable token-usage metadata."""
    if status not in _VALID_STATUSES:
        raise ValueError(f"invalid token usage status: {status}")
    if tracked_chunks < 0 or untracked_chunks < 0:
        raise ValueError("token usage chunk counts must be non-negative")
    return {
        "status": status,
        "tracked_chunks": int(tracked_chunks),
        "untracked_chunks": int(untracked_chunks),
    }


def normalize_token_usage(
    value: object,
    *,
    default_status: TokenUsageStatus = "legacy",
) -> dict:
    """Normalize metadata from disk without rejecting older files."""
    if not isinstance(value, Mapping):
        return token_usage(default_status)
    status = value.get("status")
    if status not in _VALID_STATUSES:
        status = default_status
    tracked = value.get("tracked_chunks", 0)
    untracked = value.get("untracked_chunks", 0)
    if not isinstance(tracked, int) or isinstance(tracked, bool) or tracked < 0:
        tracked = 0
    if not isinstance(untracked, int) or isinstance(untracked, bool) or untracked < 0:
        untracked = 0
    return token_usage(
        status,
        tracked_chunks=tracked,
        untracked_chunks=untracked,
    )


def combine_token_usage(
    payloads: Iterable[Mapping],
    *,
    missing_status: TokenUsageStatus = "unavailable",
) -> dict:
    """Combine chunk metadata into one run-level completeness state.

    A missing metadata object on a chunk means the host did not expose usage,
    not that the chunk consumed zero tokens.
    """
    tracked = 0
    untracked = 0
    seen = False
    saw_legacy = False
    for payload in payloads:
        seen = True
        usage = normalize_token_usage(
            payload.get("token_usage"),
            default_status=missing_status,
        )
        status = usage["status"]
        if status == "legacy":
            saw_legacy = True
        tracked += usage["tracked_chunks"]
        untracked += usage["untracked_chunks"]
        if status == "complete" and usage["tracked_chunks"] == 0:
            tracked += 1
        elif status == "unavailable" and usage["untracked_chunks"] == 0:
            untracked += 1

    if not seen:
        return token_usage("not-used")
    if saw_legacy:
        return token_usage(
            "legacy",
            tracked_chunks=tracked,
            untracked_chunks=untracked,
        )
    if tracked and untracked:
        status: TokenUsageStatus = "partial"
    elif tracked:
        status = "complete"
    elif untracked:
        status = "unavailable"
    else:
        status = "not-used"
    return token_usage(
        status,
        tracked_chunks=tracked,
        untracked_chunks=untracked,
    )


def format_token_usage(input_tokens: int, output_tokens: int, usage: object) -> str:
    """Render honest token usage for reports and terminal summaries."""
    meta = normalize_token_usage(usage)
    status = meta["status"]
    tracked = meta["tracked_chunks"]
    untracked = meta["untracked_chunks"]
    if status == "unavailable":
        return (
            "unavailable"
            f" ({tracked} tracked, {untracked} untracked chunk"
            f"{'' if untracked == 1 else 's'})"
        )
    known = f"{input_tokens:,} input · {output_tokens:,} output"
    if status == "partial":
        return (
            f"{known} known (partial: {tracked} tracked, "
            f"{untracked} untracked chunk{'' if untracked == 1 else 's'})"
        )
    if status == "not-used":
        return f"{known} (LLM not used)"
    if status == "legacy":
        return f"{known} (legacy record; completeness unknown)"
    return known


def append_cost_run(
    cost: object,
    *,
    input_tokens: int,
    output_tokens: int,
    files: int,
    usage: object,
    date: str | None = None,
) -> dict:
    """Append a run while upgrading old run records to ``legacy`` metadata."""
    if not isinstance(cost, dict):
        cost = {}
    runs = cost.get("runs")
    if not isinstance(runs, list):
        runs = []
    normalized_runs = []
    for run in runs:
        if not isinstance(run, dict):
            continue
        normalized = dict(run)
        normalized["token_usage"] = normalize_token_usage(
            run.get("token_usage"),
            default_status="legacy",
        )
        normalized_runs.append(normalized)

    meta = normalize_token_usage(usage, default_status="legacy")
    normalized_runs.append(
        {
            "date": date or datetime.now(timezone.utc).isoformat(),
            "input_tokens": int(input_tokens),
            "output_tokens": int(output_tokens),
            "files": int(files),
            "token_usage": meta,
        }
    )
    return {
        **cost,
        "runs": normalized_runs,
        "total_input_tokens": sum(
            int(run.get("input_tokens", 0) or 0) for run in normalized_runs
        ),
        "total_output_tokens": sum(
            int(run.get("output_tokens", 0) or 0) for run in normalized_runs
        ),
    }
