# Graphify Router Skill Validation

**Date**: 2026-06-30
**Spec**: `.specs/features/graphify-router-skill/spec.md`
**Diff range**: `45edb5e..fcc9232` plus current working-tree T8 corrections
**Verifier**: independent Verifier (author != verifier)
**Verdict**: PASS

---

## Task Completion

| Task | Status | Notes |
| --- | --- | --- |
| T1 | Done | `23983ce`; router size and marker characterization tests. |
| T2 | Done | `7d99cf8`; reference completeness and pointer tests. |
| T3 | Done | `ca399cd`; full build procedure moved to `build.md`. |
| T4 | Done | Covered by `ca399cd`; graph-first router and command map rendered. |
| T5 | Done | Covered by `ca399cd`; 148 generated artifacts are synchronized. |
| T6 | Done | `df70a02`; install/reference coverage. |
| T7 | Done | `fcc9232`; Claude and Codex before/after measurements recorded. |
| T8 | Done | Functional gates, graph refresh, traceability update, and independent validation pass; the atomic closure commit contains this report. |

## Spec-Anchored Acceptance Criteria

| Requirement | Spec-defined outcome | `file:line` + assertion expression | Result |
| --- | --- | --- | --- |
| GRS-01 | An existing graph and natural-language codebase question route immediately to `graphify query "<question>"`, before build detection; heavy procedure bodies remain out of the split core. | `tests/test_skillgen.py:386` - `assert "**Fast path ... existing graph:**" in core`; `:387` - `assert 'Run graphify query ... immediately.' in core`; `:388` - `assert "Do not run detect. Do not check corpus size." in core`; `:389` - fast path index is before `references/build.md`; `:404` - `assert leaked == {}`. | PASS |
| GRS-02 | `query`, `path`, and `explain` remain discoverable in the router while detailed traversal lives in `query.md`. | `tests/test_skillgen.py:390-393` - exact query/path/explain command markers and `references/query.md`; `:94` and `:99` - exact path/explain headings and commands required in the reference; `:428-433` - each reference and marker must exist. | PASS |
| GRS-03 | Bare/path/GitHub/deep/video/large-corpus builds route to complete build procedures; update, exports, add/watch, and hooks route to their matching references. | `tests/test_skillgen.py:103-107` defines the complete expected build-router row, co-locating `/graphify`, path, GitHub, deep/full-build intents, and `references/build.md`; `:424-427` asserts that exact row is present; `:428-433` verifies the rendered reference and procedure markers. The focused test passed. | PASS |
| GRS-04 | Generator check, audit coverage, schema singleton, monolith roundtrip, and always-on roundtrip pass; generated artifacts trace to fragments/platform metadata. | `tests/test_skillgen.py:157-173` - audit/check `assert problems == []`; `:560-564` - schema singleton `assert problems == []`; `:682-687` - monolith `assert problems == []`; `:827-836` - always-on `assert problems == []`; `:877-884` - every split host audit is empty. Independent CLI gate: all five commands passed, including 148 synchronized artifacts. | PASS |
| GRS-05 | Install stages `SKILL.md`, one version stamp, and all references; reinstall removes stale files; uninstall removes only the skill tree; the wheel contains every split payload including `agents`. | `tests/test_install_references.py:82-88` - installed body/sidecars exist and no staging dir remains; `:97-99` - exactly one version stamp; `:115-118` - stale reference removed and current references present; `:131-134` - uninstall removes the skill tree; `:448-459` - no missing bodies/references and exact totals are 16 bodies and 126 references. | PASS |
| GRS-06 | Claude and Codex before/after counts are recorded, every split core is at least 40% smaller, and heavy-marker reintroduction fails tests. | `tests/test_skillgen.py:29-34` records Claude/Codex `4645 -> 1214`; `:407-415` - `assert current <= baseline * 0.60`; `:396-404` - any heavy marker produces a non-empty `leaked` map and fails. | PASS |

**Status**: 6/6 requirements fully verified. No spec-precision gap was found.

## Discrimination Sensor

All mutations were made only in scratch copies under `/tmp`; the real working tree was not mutated.

| Mutation | Target | Focused test and observed result | Result |
| --- | --- | --- | --- |
| 1 | Replaced the graph-first fast path in `tools/skillgen/fragments/core/core.md:50` with detect-first behavior. | `test_split_router_keeps_graph_first_query_inline` failed at `tests/test_skillgen.py:382` because the immediate-query assertion was absent. | KILLED |
| 2 | Replaced the primary `/graphify` -> `references/build.md` target with `Continue with the inline router` while leaving auxiliary build-reference mentions intact. | Reverification in scratch failed at `tests/test_skillgen.py:425`: `[claude] route 'build' must keep intent and reference in the same router row`. This independently confirms the new co-location assertion kills the prior survivor. | KILLED |
| 3 | Removed `graphify/skill-agents.md` from the scratch wheel payload. | `test_built_wheel_ships_the_full_skill_payload` failed at `tests/test_install_references.py:449` with `wheel is missing skill bodies: ['skill-agents.md']`. | KILLED |

**Sensor depth**: lightweight, 3 behavior-level mutations.
**Result**: 3/3 killed - PASS.

## Edge Cases

- [x] Missing/renamed reference pointers: all split cores compare pointer names with rendered sidecars at `tests/test_skillgen.py:300-308`.
- [x] Host-specific dispatch/hooks: `agents` wording and leakage exclusions are asserted at `tests/test_skillgen.py:1094-1115`; per-host audits are empty at `:877-884`.
- [x] Monolith platforms remain single-file and roundtrip-clean at `tests/test_skillgen.py:682-687`.
- [x] Reinstall removes stale fragments and interrupted staging self-heals at `tests/test_install_references.py:102-118` and `tests/test_install_roundtrip.py:274-293`.
- [x] Failed sidecar staging preserves the previous good references at `tests/test_install_roundtrip.py:296-318`.
- [x] Preexisting root `.gitignore` and `AGENTS.md` edits are outside `45edb5e..fcc9232`; no feature commit includes them.
- [x] Primary build-route association is discriminated from incidental `build.md` mentions by the exact-row assertion at `tests/test_skillgen.py:424-427`.

## Gate Check

| Gate | Result |
| --- | --- |
| Quick | Orchestrator: `65 passed` in `tests/test_skillgen.py`; independent focused GRS-03 test: `1 passed`. |
| Skillgen | `--check`: 148 artifacts; audit coverage, schema singleton, monolith roundtrip, and always-on roundtrip all passed. |
| Install | `167 passed, 1 skipped`; wheel `agents` test also passed independently. |
| Full | Restricted-sandbox run was interrupted after hanging in the known Starlette `TestClient`/local-binding block. Secondary orchestrator evidence: `2541 passed, 3 skipped` outside the sandbox. |

Graph refresh evidence from the orchestrator: `graphify update .` completed with 10056 nodes and 15995 edges.

- **Test count before feature**: 2524 collected at `45edb5e`.
- **Test count after feature**: 2544 collected.
- **Delta**: +20 tests; no test-count decrease.
- **Skipped tests**:
  - `tests/test_falkordb_integration.py:53`: no FalkorDB at localhost:6379.
  - `tests/test_falkordb_integration.py:75`: no FalkorDB at localhost:6379.
  - `tests/test_install_references.py:250`: all progressive bundles ship, so no pre-wave fallback candidate exists.
- **Failures outside the sensor**: none when local TestClient binding is permitted.

## Code Quality

| Principle | Status |
| --- | --- |
| Minimum code and no scope creep | PASS - source changes are limited to skillgen fragments/generator and directly related tests; the large file count is generated output. |
| Surgical changes | PASS - unrelated root edits are not in the feature commits. |
| Matches existing generator patterns | PASS - `Platform.reference_sources()` and generated snapshots remain the only artifact flow. |
| Spec-anchored outcomes | PASS - GRS-03 now asserts the complete intent/target row. |
| Per-layer coverage | PASS. |
| No unclaimed tests | PASS for the reviewed feature diff. |
| Documented guidelines | PASS - `AGENTS.md`, `tasks.md`, and the skillgen source-of-truth contract were followed. |
| Diff hygiene | PASS - `git diff --check 45edb5e` is clean. |

## Administrative Closure

Task and traceability files are updated. The atomic T8 closure commit contains this report and excludes preexisting root changes.

## Requirement Traceability Update

This Verifier was not authorized to edit `spec.md`; the recommended status update is:

| Requirement | Current status | Verified status |
| --- | --- | --- |
| GRS-01 | Pending | Verified |
| GRS-02 | Pending | Verified |
| GRS-03 | Pending | Verified |
| GRS-04 | Pending | Verified |
| GRS-05 | Pending | Verified |
| GRS-06 | Complete | Verified |

## Summary

**Overall**: READY - PASS

The router implementation satisfies all six requirements, generated artifacts are synchronized, install/package integrity passes including `agents`, the measured reduction exceeds 40%, and all three behavioral mutations are killed. The full suite passes when local HTTP binding is allowed, and T8 administrative state is closed.
