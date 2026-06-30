# Agents Install Gitignore Validation

**Date**: 2026-06-30
**Spec**: `.specs/features/agents-install-gitignore/spec.md`
**Diff range**: `08417cd..5851f4d`
**Verifier**: standalone fresh-eyes fallback (no subagents by user instruction)

## Spec-Anchored Acceptance Criteria

| Requirement | Evidence | Result |
| --- | --- | --- |
| GIG-01/02 | `tests/test_agents_platform.py:213` — reads created file; lines 214-217 assert local ignores and labels exception | PASS |
| GIG-03 | `tests/test_agents_platform.py:234` — lines 235-240 assert user-rule preservation, broad-rule removal, deduplication, and labels exception | PASS |
| GIG-04 | `tests/test_agents_platform.py:195` and `:202` — second install is byte-identical with one marker | PASS |
| GIG-05 | `tests/test_agents_platform.py:269` — corrupt file bytes unchanged; lines 270-271 assert AGENTS continuation and explicit error | PASS |
| GIG-06 | `tests/test_agents_platform.py:254` — `--no-gitignore` preserves exact bytes | PASS |
| GIG-07 | `tests/test_agents_platform.py:284` — uninstall preserves exact managed block bytes | PASS |

## Gate

- Focused: 114 passed.
- Skillgen: 148 generated artifacts match.
- Full after rollout remediation: 2549 passed, 3 known skips; baseline did not decrease.

## Discrimination Sensor

- Mutation: replaced `_ensure_graphify_gitignore()` with a no-op in a detached
  `/tmp` worktree.
- Result: killed; three focused tests failed because creation, corruption
  reporting, and uninstall lifecycle were no longer satisfied.

## Code Quality

Surgical changes, no unrelated refactor, canonical block is single-purpose,
tests map directly to GIG-01..07, and the README/help describe the same public
contract.

**Overall**: PASS

## Rollout Remediation

The first self-host rollout exposed that the unmarked Graphify section updater
consumed an HTML bridge marker immediately before the next H2. The replacement
boundary now preserves such markers. `tests/test_agents_platform.py` covers the
Graphify→ProjectMem sequence. A second rollout review found case-sensitive H2
matching; the updater now adopts `## Graphify` without duplication. The repeated
full gate passed 2549 tests.
