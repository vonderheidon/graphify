# Graphify Router Skill Specification

**Status**: Complete
**Source plan**: `/home/jefferson/Dev/projetos/geral/handoffs/context-optimization/03-graphify.md`

## Problem Statement

The installable Graphify skill currently carries too much runbook detail in the initial skill body, so ordinary codebase questions pay context cost for build/update/export procedures that are not needed. The feature turns the public `graphify` skill into a lean router that keeps graph-first query behavior immediately available while moving heavier procedures into progressive references loaded only when the user asks for them.

## Goals

- [x] Reduce the initial generated `SKILL.md` bodies to graph-first routing, command map, and honesty/safety rules while preserving every existing capability through references.
- [x] Preserve default query/explain/path behavior for existing `graphify-out/` graphs without loading the full build runbook.
- [x] Keep explicit build, update, add/watch, export, hook, install, and uninstall paths functional through valid sidecar references.
- [x] Validate generator drift, reference coverage, package contents, install/upgrade/uninstall behavior, and measurable skill-size reduction.

## Out of Scope

| Feature | Reason |
| --- | --- |
| Changes to `youtube-content-extractor` | Cockpit requires one active repo at a time. |
| Changes to `projectmem` | This feature is local to `graphify-v8`. |
| Publishing or opening a PR | User did not authorize remote publication. |
| Mixing preexisting `.gitignore` or root `AGENTS.md` changes into this feature | Cockpit says those changes predate this work and must be preserved. |
| Running `uv tool install --reinstall` as an implicit side effect | Reinstall must be explicit and reversible. |
| Removing any Graphify command capability | The goal is progressive disclosure, not behavior deletion. |

---

## Assumptions & Open Questions

Every ambiguity is resolved or recorded here; none is left silently unclear.

| Assumption / decision | Chosen default | Rationale | Confirmed? |
| --- | --- | --- | --- |
| Initial router size target | Treat success as at least 40% fewer words in the generated core skill body for split platforms, measured against the current committed output before edits. | The plan asks for context reduction but gives no number; 40% is large enough to prove the change without forcing arbitrary token golf. | y |
| Progressive references | Keep the existing eight rendered references as the minimum: `github-and-merge.md`, `update.md`, `exports.md`, `transcribe.md`, `add-watch.md`, `extraction-spec.md`, `query.md`, `hooks.md`; add `build.md` only if default build detail leaves the router. | The current generator already renders eight references; the plan explicitly mentions moving full build into a reference. | y |
| Query path | Keep enough inline content for `/graphify query`, `/graphify path`, and `/graphify explain` discovery, but route advanced traversal/fallback details to `references/query.md`. | The cockpit's success criterion is that common codebase questions avoid the build runbook. | y |
| Skill platforms | Apply the router split to every platform currently declared as `bucket = "split"` in `tools/skillgen/platforms.toml`; leave monolith platforms unchanged unless tests require compatibility stubs. | This follows the existing generator architecture and limits blast radius. | y |
| Reinstall validation | Do not reinstall the user's global `uv tool` during implementation; validate package/install behavior with tests and document any optional manual reinstall separately. | Cockpit guardrail says global reinstall is explicit only. | y |

**Open questions:** none -- all unresolved choices are recorded as assumptions above.

---

## User Stories

### P1: Graph-First Router Core - MVP

**User Story**: As an agent using Graphify, I want the installed skill to route codebase questions to the existing graph without loading build/update/export runbooks so that common exploration consumes less context.

**Why P1**: This is the primary context-optimization win.

**Acceptance Criteria**:

1. WHEN the user asks a natural-language codebase question and `graphify-out/graph.json` exists THEN the generated skill SHALL instruct the agent to run `graphify query "<question>"` before any build detection flow.
2. WHEN the user asks for `/graphify path` or `/graphify explain` THEN the generated skill SHALL expose those commands in the router and route detailed traversal behavior to `references/query.md`.
3. WHEN the generated split-platform core is measured before and after this feature THEN the new core SHALL be at least 40% smaller by word count while keeping command discoverability.
4. WHEN the generated split-platform core is inspected THEN it SHALL NOT inline build, update, exports, hook, add/watch, or extraction-schema procedure bodies except for concise route pointers.

**Independent Test**: Render a split platform and assert the core contains graph-first query routing and command pointers while excluding distinctive markers from heavy runbooks.

### P1: Build And Update Capabilities Survive

**User Story**: As an agent running explicit Graphify build or update commands, I want the full procedure available on demand so that progressive disclosure does not remove functionality.

**Why P1**: Context savings are only acceptable if existing workflows still work.

**Acceptance Criteria**:

1. WHEN the user invokes a full build path (`/graphify`, `/graphify <path>`, GitHub URL, deep mode, video, or large corpus) THEN the generated skill SHALL route to the reference that contains the complete build pipeline.
2. WHEN the user invokes `--update` or `--cluster-only` THEN the generated skill SHALL route to `references/update.md`.
3. WHEN the user invokes exports (`--wiki`, `--neo4j`, `--falkordb`, `--svg`, `--graphml`, `--mcp`) THEN the generated skill SHALL route to `references/exports.md`.
4. WHEN the user invokes `/graphify add`, `--watch`, or hook/native AGENTS integration THEN the generated skill SHALL route to the matching `add-watch.md` or `hooks.md` reference.

**Independent Test**: Render each split platform and verify every router pointer resolves to a packaged reference with the required procedure markers.

### P1: Generator-Only Artifact Flow

**User Story**: As a maintainer, I want all skill body and reference changes to flow through `tools/skillgen` so generated artifacts, expected snapshots, and platform variants stay consistent.

**Why P1**: The repo has anti-drift tooling and many platform-specific render outputs.

**Acceptance Criteria**:

1. WHEN `uv run --frozen python -m tools.skillgen --check` runs THEN it SHALL pass with committed artifacts and expected snapshots synchronized.
2. WHEN `uv run --frozen python -m tools.skillgen --audit-coverage` runs THEN it SHALL pass without silently dropping pre-split headings.
3. WHEN `uv run --frozen python -m tools.skillgen --schema-singleton`, `--monolith-roundtrip`, and `--always-on-roundtrip` run THEN they SHALL pass.
4. WHEN generated artifacts are changed THEN their source changes SHALL be traceable to `tools/skillgen/fragments/` or `tools/skillgen/platforms.toml`.

**Independent Test**: Run the skillgen check/audit/roundtrip commands from CI.

### P1: Install Package Integrity

**User Story**: As a user installing Graphify for supported agents, I want the lean skill and references sidecar to install, upgrade, and uninstall correctly.

**Why P1**: A router that points to missing references would fail at runtime.

**Acceptance Criteria**:

1. WHEN a split-platform install runs in tests THEN `SKILL.md`, `.graphify_version`, and all referenced sidecar files SHALL be installed together.
2. WHEN reinstall runs in tests THEN stale sidecar fragments SHALL be removed and current references SHALL replace them atomically.
3. WHEN uninstall runs in tests THEN the skill directory and sidecar references SHALL be removed without touching unrelated global or project skills.
4. WHEN package/wheel tests inspect included files THEN all split-platform skill bodies and references SHALL be present.

**Independent Test**: Run focused install/reference/roundtrip/agents-platform tests.

### P2: Measurement And Documentation

**User Story**: As a maintainer reviewing the change, I want the size reduction and routing behavior documented so that the benefit is visible and future edits do not regress it accidentally.

**Why P2**: Measurement helps prove the feature achieved its goal and guards against future bloat.

**Acceptance Criteria**:

1. WHEN the task completes THEN implementation notes or tests SHALL record before/after word counts for at least the Claude and Codex split cores.
2. WHEN a future edit re-inlines heavy runbook markers into the router THEN tests SHALL fail.
3. WHEN README or developer docs mention skill generation THEN any changed wording SHALL continue to tell maintainers to edit fragments and run skillgen.

**Independent Test**: Unit tests assert size and marker exclusions; docs review confirms source-of-truth wording if docs are touched.

## Edge Cases

- WHEN a reference pointer is renamed THEN the render/check tests SHALL fail if the generated core points at a non-rendered file.
- WHEN a split platform uses host-specific dispatch or hooks wording THEN the rendered router SHALL keep that host's dispatch and hooks target intact.
- WHEN a platform remains monolith-only THEN roundtrip tests SHALL prove it did not unintentionally change.
- WHEN `graphify-out/` files are dirty before implementation THEN they SHALL not be treated as blockers and SHALL not be included unless the feature explicitly updates the graph.
- WHEN root `.gitignore` or root `AGENTS.md` contain preexisting edits THEN this feature SHALL avoid modifying or staging them without explicit approval.

## Implicit-Requirement Sweep

| Dimension | Resolution |
| --- | --- |
| Input validation & bounds | Requirement: router pointers must resolve to real packaged references; size measurement uses deterministic word counts. |
| Failure / partial-failure states | Requirement: install/reinstall/uninstall tests cover missing/stale sidecars and package integrity. |
| Idempotency / retry / duplicate handling | Requirement: skillgen render remains idempotent and reinstall replaces stale references atomically. |
| Auth boundaries & rate limits | N/A because this feature changes skill documentation/routing, not credentialed API behavior. |
| Concurrency / ordering | Requirement: generated artifacts derive from one source-of-truth flow to avoid drift across platforms. |
| Data lifecycle / expiry | N/A because no runtime data storage is introduced. |
| Observability | Requirement: measurement records before/after skill core size. |
| External-dependency failure | Requirement: no implicit `uv tool` reinstall; validation uses local repo tests and frozen commands. |
| State-transition integrity | Requirement: install -> reinstall -> uninstall preserves correct sidecar state and removes stale fragments. |

## Requirement Traceability

| Requirement ID | Story | Phase | Status |
| --- | --- | --- | --- |
| GRS-01 | P1: Graph-First Router Core | T1/T4 | Verified |
| GRS-02 | P1: Graph-First Router Core | T1/T2/T4 | Verified |
| GRS-03 | P1: Build And Update Capabilities Survive | T2/T3 | Verified |
| GRS-04 | P1: Generator-Only Artifact Flow | T2/T3/T5 | Verified |
| GRS-05 | P1: Install Package Integrity | T6/T8 | Verified |
| GRS-06 | P2: Measurement And Documentation | T7 | Verified |

**Coverage:** 6 total, 6 verified.

## Success Criteria

- [x] Common codebase questions use `graphify query` from the router without loading the full build runbook.
- [x] Explicit build/update/export/add/watch/hook flows still have complete on-demand references.
- [x] Skillgen, coverage, roundtrip, focused install tests, and full pytest gate pass.
- [x] Split-platform core size reduction is measured and meets the 40% assumption.
- [x] Implementation remains isolated to Graphify files and does not mix preexisting root `.gitignore` or `AGENTS.md` edits.
