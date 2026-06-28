from graphify.token_usage import (
    append_cost_run,
    combine_token_usage,
    format_token_usage,
    token_usage,
)


def test_host_usage_is_complete_with_exact_totals():
    chunks = [
        {
            "input_tokens": 123,
            "output_tokens": 45,
            "token_usage": token_usage("complete", tracked_chunks=1),
        }
    ]
    assert combine_token_usage(chunks) == {
        "status": "complete",
        "tracked_chunks": 1,
        "untracked_chunks": 0,
    }
    assert format_token_usage(123, 45, chunks[0]["token_usage"]) == (
        "123 input · 45 output"
    )


def test_missing_host_usage_is_unavailable_not_zero():
    usage = combine_token_usage([{"input_tokens": 0, "output_tokens": 0}])
    assert usage["status"] == "unavailable"
    assert usage["untracked_chunks"] == 1
    rendered = format_token_usage(0, 0, usage)
    assert rendered.startswith("unavailable")
    assert "0 input" not in rendered


def test_mixed_chunks_are_partial_and_keep_known_totals():
    chunks = [
        {"token_usage": token_usage("complete", tracked_chunks=1)},
        {},
    ]
    usage = combine_token_usage(chunks)
    assert usage == {
        "status": "partial",
        "tracked_chunks": 1,
        "untracked_chunks": 1,
    }
    assert "120 input · 30 output known" in format_token_usage(120, 30, usage)


def test_no_chunks_is_legitimate_not_used_zero():
    usage = combine_token_usage([])
    assert usage["status"] == "not-used"
    assert format_token_usage(0, 0, usage) == "0 input · 0 output (LLM not used)"


def test_old_cost_records_are_preserved_as_legacy():
    old = {
        "runs": [
            {
                "date": "2026-01-01T00:00:00+00:00",
                "input_tokens": 0,
                "output_tokens": 0,
                "files": 2,
            }
        ],
        "total_input_tokens": 0,
        "total_output_tokens": 0,
    }
    updated = append_cost_run(
        old,
        input_tokens=10,
        output_tokens=4,
        files=1,
        usage=token_usage("complete", tracked_chunks=1),
        date="2026-01-02T00:00:00+00:00",
    )
    assert updated["runs"][0]["token_usage"]["status"] == "legacy"
    assert updated["runs"][1]["token_usage"]["status"] == "complete"
    assert updated["total_input_tokens"] == 10
    assert updated["total_output_tokens"] == 4
