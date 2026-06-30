# Graphify Router Skill Tasks

## Execution Protocol (MANDATORY -- do not skip)

Implement these tasks with the `tlc-spec-driven` skill: **activate it by name and follow its Execute flow and Critical Rules.** Do not search for skill files by filesystem path. The skill is the source of truth for the full flow (per-task cycle, sub-agent delegation, adequacy review, Verifier, discrimination sensor).

**If the skill cannot be activated, STOP and tell the user -- do not proceed without it.**

---

**Design**: `.specs/features/graphify-router-skill/design.md`
**Status**: Complete

---

## Test Coverage Matrix

> Generated from codebase, project guidelines, and spec -- confirm before Execute. Guidelines found: `README.md`, `pyproject.toml`, `.github/workflows/ci.yml`, `tests/test_skillgen.py`, `tests/test_install_references.py`, `tests/test_agents_platform.py`.

| Code Layer | Required Test Type | Coverage Expectation | Location Pattern | Run Command |
| --- | --- | --- | --- | --- |
| Skill generator fragments and render logic | unit/integration | All changed router/reference behavior maps 1:1 to `GRS-*`; pointer validity, marker exclusions, size reduction, idempotent render, and per-platform render drift covered. | `tests/test_skillgen.py` | `uv run --frozen pytest tests/test_skillgen.py -q --tb=short` |
| Install and sidecar lifecycle | unit/integration | Install, reinstall, uninstall, missing sidecar warning, platform-specific destination, and package file inclusion for any new reference. | `tests/test_install_references.py`, `tests/test_install_roundtrip.py`, `tests/test_install_upgrade.py`, `tests/test_agents_platform.py`, `tests/test_install.py` | `uv run --frozen pytest tests/test_install_references.py tests/test_install_roundtrip.py tests/test_install_upgrade.py tests/test_agents_platform.py tests/test_install.py -q --tb=short` |
| Generated artifacts and expected snapshots | integration/build gate | `--check`, audit coverage, schema singleton, monolith roundtrip, always-on roundtrip all pass; generated files are synchronized with fragments. | `tools/skillgen/**`, `graphify/skill*.md`, `graphify/skills/**`, `tools/skillgen/expected/**` | `uv run --frozen python -m tools.skillgen --check && uv run --frozen python -m tools.skillgen --audit-coverage && uv run --frozen python -m tools.skillgen --schema-singleton && uv run --frozen python -m tools.skillgen --monolith-roundtrip && uv run --frozen python -m tools.skillgen --always-on-roundtrip` |
| Documentation-only updates | none/build gate | If docs are changed, verify source-of-truth wording and run build/full gates; no separate doc test required. | `README.md`, docs under `docs/` | build gate only |

## Parallelism Assessment

> Generated from codebase -- confirm before Execute.

| Test Type | Parallel-Safe? | Isolation Model | Evidence |
| --- | --- | --- | --- |
| Skillgen render tests | Yes | Pure render helpers read fragments and compare strings; no shared runtime state. | `tests/test_skillgen.py` uses `gen.render_all()` and in-memory assertions. |
| Install lifecycle tests | Yes within pytest process, but run sequentially with the focused command | Tests use `tmp_path`, patched `Path.home`, and temp cwd; some fixtures temporarily move package bundle dirs during a single test. | `tests/test_install_references.py` fake bundle fixture restores on teardown. |
| Skillgen CLI gates | No | Commands compare and read/write generated outputs and snapshots in the working tree. | `tools/skillgen/gen.py` `write_artifacts`, `check`, `bless`; run sequentially. |
| Full pytest | No | Broad suite may include filesystem/package side effects; run as final sequential gate. | README/CI full test command. |

## Gate Check Commands

> Generated from codebase -- confirm before Execute.

| Gate Level | When to Use | Command |
| --- | --- | --- |
| Quick | After task changes only skillgen unit assertions or fragments | `uv run --frozen pytest tests/test_skillgen.py -q --tb=short` |
| Install | After task changes install/package sidecar behavior | `uv run --frozen pytest tests/test_install_references.py tests/test_install_roundtrip.py tests/test_install_upgrade.py tests/test_agents_platform.py tests/test_install.py -q --tb=short` |
| Skillgen | After any fragment/platform/generated artifact change | `uv run --frozen python -m tools.skillgen --check && uv run --frozen python -m tools.skillgen --audit-coverage && uv run --frozen python -m tools.skillgen --schema-singleton && uv run --frozen python -m tools.skillgen --monolith-roundtrip && uv run --frozen python -m tools.skillgen --always-on-roundtrip` |
| Full | Before final validation | `uv run --frozen pytest tests/ -q --tb=short` |

---

## Execution Plan

### Phase 1: Characterization And Guards (Sequential)

```text
T1 -> T2
```

### Phase 2: Router And References (Sequential)

```text
T2 -> T3 -> T4 -> T5
```

### Phase 3: Generated Artifacts And Install Coverage (Sequential)

```text
T5 -> T6 -> T7
```

### Phase 4: Final Gates And Graph Refresh (Sequential)

```text
T7 -> T8
```

> This plan has more than 3 phases. Before Execute, `tlc-spec-driven` requires offering one worker per phase, sequentially, and waiting for user confirmation before any sub-agent dispatch.

## Task Breakdown

### T1: Add Router Size And Marker Characterization Tests

**What**: Update skillgen tests to express the new router behavior before implementation.
**Where**: `tests/test_skillgen.py`
**Depends on**: None
**Reuses**: Existing `_claude_artifacts()`, `_platform_artifacts()`, render helpers, marker-exclusion tests.
**Requirement**: GRS-01, GRS-02, GRS-06

**Tools**:

- MCP: NONE
- Skill: `tlc-spec-driven`

**Done when**:

- [x] Tests assert graph-first query routing remains inline.
- [x] Tests assert heavy build/update/export/add-watch/hooks/extraction markers are absent from split cores.
- [x] Tests assert split core word count is at least 40% smaller than a documented baseline.
- [x] Quick gate fails before implementation for the intended reasons, then passes after later tasks.

**Tests**: unit/integration
**Gate**: Quick

**Commit**: `23983ce` `test(skillgen): characterize graphify router core`; `c281a46` sharpened marker guards after subagent review.

---

### T2: Add Reference Completeness And Pointer Tests

**What**: Extend tests so every router pointer resolves and heavy procedures live in the expected references.
**Where**: `tests/test_skillgen.py`
**Depends on**: T1
**Reuses**: `test_reference_pointers_in_core_resolve_to_real_fragments`, `test_eight_references_render_for_claude`, per-platform render helpers.
**Requirement**: GRS-03, GRS-04

**Tools**:

- MCP: NONE
- Skill: `tlc-spec-driven`

**Done when**:

- [x] Tests fail if core points at a missing `references/*.md`.
- [x] Tests cover `query`, `path`, `explain`, build, update, exports, add/watch, hooks, transcribe, and extraction-schema routes.
- [x] Tests assert any new `build.md` reference renders for split platforms if build detail moves out of core.
- [x] Quick gate fails before implementation for the intended reasons, then passes after later tasks.

**Tests**: unit/integration
**Gate**: Quick

**Commit**: `7d99cf8` `test(skillgen): guard router reference coverage`

---

### T3: Re-home Full Build Procedure Into References

**What**: Move explicit full-build procedure detail out of the split router core and into an on-demand reference, preserving command semantics.
**Where**: `tools/skillgen/fragments/core/core.md`, `tools/skillgen/fragments/references/shared/build.md` if introduced, `tools/skillgen/gen.py` if reference mapping changes.
**Depends on**: T2
**Reuses**: Existing build steps in `core.md`, `_SHARED_REFERENCES`, `Platform.reference_sources()`.
**Requirement**: GRS-01, GRS-03, GRS-04

**Tools**:

- MCP: NONE
- Skill: `tlc-spec-driven`

**Done when**:

- [x] Router core has concise route pointers for explicit build flows instead of full procedural body.
- [x] Full build, GitHub/multi-path, large corpus, video/transcribe, extraction, build, label, export, cleanup, and report procedures remain available in references.
- [x] Every new or changed reference is rendered for all split platforms.
- [x] Quick gate passes.

**Tests**: unit/integration
**Gate**: Quick

**Commit**: `ca399cd` `feat(skillgen): route full build through references`

---

### T4: Tighten Query Router And Command Map

**What**: Ensure common graph queries stay inline while advanced traversal detail stays in `query.md`.
**Where**: `tools/skillgen/fragments/core/core.md`, `tools/skillgen/fragments/query-stub/default.md`, `tools/skillgen/fragments/references/query/default.md`
**Depends on**: T3
**Reuses**: Existing query stub and query reference.
**Requirement**: GRS-01, GRS-02

**Tools**:

- MCP: NONE
- Skill: `tlc-spec-driven`

**Done when**:

- [x] Existing-graph natural-language questions route directly to `graphify query "<question>"`.
- [x] `/graphify path` and `/graphify explain` are discoverable in the core and detailed in `query.md`.
- [x] The command map covers update, exports, add/watch, hooks, transcribe, and build references without procedural duplication.
- [x] Quick gate passes.

**Tests**: unit/integration
**Gate**: Quick

**Commit**: Covered by `ca399cd` `feat(skillgen): route full build through references`; no additional artifact diff was needed. Quick gate: 65 passed.

---

### T5: Regenerate Skill Artifacts And Expected Snapshots

**What**: Render committed skill artifacts and expected snapshots from the updated generator/fragments.
**Where**: `graphify/skill*.md`, `graphify/skills/*/references/*.md`, `tools/skillgen/expected/*`
**Depends on**: T4
**Reuses**: `python -m tools.skillgen`, `python -m tools.skillgen --bless`.
**Requirement**: GRS-04

**Tools**:

- MCP: NONE
- Skill: `tlc-spec-driven`

**Done when**:

- [x] Generated artifacts are synchronized with fragments.
- [x] Expected snapshots are synchronized.
- [x] Skillgen gate passes.
- [x] No root `.gitignore` or root `AGENTS.md` preexisting change is modified or staged by this task.

**Tests**: integration/build gate
**Gate**: Skillgen

**Commit**: Covered by `ca399cd` `feat(skillgen): route full build through references`; `tools.skillgen --check` reported 148 artifacts match committed output and expected/.

---

### T6: Extend Install And Package Sidecar Tests

**What**: Update install/package tests for any changed reference set and router sidecar integrity.
**Where**: `tests/test_install_references.py`, `tests/test_install_roundtrip.py`, `tests/test_install_upgrade.py`, `tests/test_agents_platform.py`, `tests/test_install.py`
**Depends on**: T5
**Reuses**: Existing temp-home install helpers and fake bundle tests.
**Requirement**: GRS-05

**Tools**:

- MCP: NONE
- Skill: `tlc-spec-driven`

**Done when**:

- [x] Split-platform installs include `SKILL.md`, `.graphify_version`, and all rendered references.
- [x] Reinstall removes stale reference fragments.
- [x] Uninstall removes sidecars without touching unrelated user/project skills.
- [x] Install gate passes.

**Tests**: unit/integration
**Gate**: Install

**Commit**: `df70a02` `test(install): cover router reference sidecars`; install gate: 167 passed / 1 skipped.

---

### T7: Record Measurement And Developer Guidance

**What**: Add or update concise measurement/developer guidance if needed, without broad docs churn.
**Where**: Prefer tests or an implementation note in `tests/test_skillgen.py`; update `README.md` only if current wording becomes wrong.
**Depends on**: T6
**Reuses**: README testing/source-of-truth guidance, CI commands.
**Requirement**: GRS-06

**Tools**:

- MCP: NONE
- Skill: `tlc-spec-driven`

**Done when**:

- [x] Before/after word-count evidence for Claude and Codex split cores is captured in tests or implementation notes.
- [x] Any docs touched continue to identify `tools/skillgen/fragments/` as source of truth.
- [x] Quick and Install gates pass.

**Tests**: unit/integration or none for doc-only changes per matrix
**Gate**: Quick + Install

**Commit**: `fcc9232` `docs(skillgen): document router size guard`

---

### T8: Run Final Gates And Refresh Graph Metadata

**What**: Run final verification gates and update local graph metadata after code changes.
**Where**: repo root, `graphify-out/` if `graphify update .` changes it
**Depends on**: T7
**Reuses**: README/CI commands and project AGENTS graphify rule.
**Requirement**: GRS-01, GRS-02, GRS-03, GRS-04, GRS-05, GRS-06

**Tools**:

- MCP: NONE
- Skill: `tlc-spec-driven`, `graphify`

**Done when**:

- [x] Skillgen gate passes.
- [x] Full pytest gate passes.
- [x] `graphify update .` is run after code changes, and any graph output changes are reviewed.
- [x] `.specs/features/graphify-router-skill/validation.md` is produced by the mandatory Verifier after the last implementation task.

**Tests**: integration/build gate
**Gate**: Skillgen + Full

**Commit**: `chore(graphify): refresh router graph metadata`

---

## Parallel Execution Map

```text
Phase 1:
  T1 -> T2

Phase 2:
  T2 -> T3 -> T4 -> T5

Phase 3:
  T5 -> T6 -> T7

Phase 4:
  T7 -> T8
```

No tasks are marked `[P]` because the generator, snapshots, and package tests share the same artifact surface and should stay sequential for clean atomic commits.

## Diagram-Definition Cross-Check

| Task | Depends On (task body) | Diagram Shows | Status |
| --- | --- | --- | --- |
| T1 | None | starts Phase 1 | OK |
| T2 | T1 | T1 -> T2 | OK |
| T3 | T2 | T2 -> T3 | OK |
| T4 | T3 | T3 -> T4 | OK |
| T5 | T4 | T4 -> T5 | OK |
| T6 | T5 | T5 -> T6 | OK |
| T7 | T6 | T6 -> T7 | OK |
| T8 | T7 | T7 -> T8 | OK |

## Test Co-location Validation

| Task | Code Layer Created/Modified | Matrix Requires | Task Says | Status |
| --- | --- | --- | --- | --- |
| T1 | Skillgen render tests | unit/integration | unit/integration | OK |
| T2 | Skillgen render tests | unit/integration | unit/integration | OK |
| T3 | Generator fragments/reference mapping | unit/integration | unit/integration | OK |
| T4 | Generator fragments/query reference | unit/integration | unit/integration | OK |
| T5 | Generated artifacts/snapshots | integration/build gate | integration/build gate | OK |
| T6 | Install/package lifecycle tests | unit/integration | unit/integration | OK |
| T7 | Measurement/docs | unit/integration or none | unit/integration or none | OK |
| T8 | Final gates/graph metadata | integration/build gate | integration/build gate | OK |

## Tools And Skills To Confirm Before Execute

Available skills expected for Execute:

- `tlc-spec-driven` for per-task implementation, gates, atomic commits, and final verifier.
- `graphify` for graph refresh after code changes.

Available local tools expected:

- Filesystem editing in this repo.
- `uv run --frozen ...` commands.
- `graphify update .` after code changes.

Ask before Execute: "For each task, should I use only the local filesystem/CLI plus `tlc-spec-driven` and `graphify`, or do you want any additional MCP/tooling involved?"
