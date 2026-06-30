# STATE

## Decisions

### AD-001
- **Decision**: Skill artifacts for Graphify must be changed through `tools/skillgen` fragments and regenerated artifacts, not by hand-editing generated `graphify/skill*.md` or packaged `graphify/skills/*` outputs.
- **Reason**: The repo already treats `tools/skillgen/fragments/` and `tools/skillgen/platforms.toml` as the source of truth, with `tools.skillgen --check` and expected snapshots guarding generated output drift.
- **Trade-off**: Small copy-only edits require a generator run and snapshot review instead of a direct markdown edit.
- **Scope**: Graphify skill bodies, references sidecars, always-on instruction blocks, and installable platform skill artifacts.
- **Date**: 2026-06-30
- **Status**: active

## Handoff

- **Feature**: `.specs/features/graphify-router-skill/`
- **Phase / Task**: Phase 4 / T8 complete; feature validated
- **Completed**: T1 `23983ce`; T2 `7d99cf8`; review refinement `c281a46`; T3/T4/T5 `ca399cd`; T6 `df70a02`; T7 `fcc9232`; T8 final gates, graph refresh, wheel coverage correction, and independent validation PASS
- **In-progress** (file:line): none
- **Next step**: none for this feature; optional remote publication remains out of scope.
- **Blockers**: none; skillgen gate passed (148 artifacts), install gate passed (`167 passed, 1 skipped`), full gate passed outside the restricted HTTP sandbox (`2541 passed, 3 skipped`), and the independent Verifier passed 6/6 requirements with 3/3 mutations killed.
- **Uncommitted files**: preexisting `.gitignore`, `AGENTS.md`, `CLAUDE.md`, `.projectmem/`
- **Branch**: `v8...fork/v8`
