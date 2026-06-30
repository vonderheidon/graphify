# STATE

## Decisions

### AD-002
- **Decision**: The friendly `graphify agents install` / `graphify skills install` workflow owns a delimited shared-output policy in `.gitignore`; self-hosting can opt out with `--no-gitignore`.
- **Reason**: Repositories need the same portable distinction between shared Graphify outputs and machine-local state without hand-maintained ignore drift.
- **Trade-off**: Install now mutates one additional project file by default, while malformed markers require manual repair.
- **Scope**: Native cross-framework agents/skills installation only; uninstall intentionally leaves the ignore policy in place.
- **Date**: 2026-06-30
- **Status**: active

### AD-001
- **Decision**: Skill artifacts for Graphify must be changed through `tools/skillgen` fragments and regenerated artifacts, not by hand-editing generated `graphify/skill*.md` or packaged `graphify/skills/*` outputs.
- **Reason**: The repo already treats `tools/skillgen/fragments/` and `tools/skillgen/platforms.toml` as the source of truth, with `tools.skillgen --check` and expected snapshots guarding generated output drift.
- **Trade-off**: Small copy-only edits require a generator run and snapshot review instead of a direct markdown edit.
- **Scope**: Graphify skill bodies, references sidecars, always-on instruction blocks, and installable platform skill artifacts.
- **Date**: 2026-06-30
- **Status**: active

## Handoff

- **Feature**: `.specs/features/agents-install-gitignore/`
- **Phase / Task**: Phase 3 / T3 complete
- **Completed**: T1 `23983ce`; T2 `7d99cf8`; review refinement `c281a46`; T3/T4/T5 `ca399cd`; T6 `df70a02`; T7 `fcc9232`; T8 final gates, graph refresh, wheel coverage correction, and independent validation PASS
- **In-progress** (file:line): none
- **Next step**: T4 run full validation, discrimination sensor, and graph refresh.
- **Blockers**: none; skillgen gate passed (148 artifacts), install gate passed (`167 passed, 1 skipped`), full gate passed outside the restricted HTTP sandbox (`2541 passed, 3 skipped`), and the independent Verifier passed 6/6 requirements with 3/3 mutations killed.
- **Uncommitted files**: preexisting `.gitignore`, `AGENTS.md`, `CLAUDE.md`, `.projectmem/`
- **Branch**: `v8...fork/v8`
