# Tasks

## Phase 1 — Contract

- [ ] T1 Specify policy and decision state.
  - Verify: spec covers GIG-01..07 and edge cases.
  - Gate: documentation inspection.

## Phase 2 — Product

- [ ] T2 Implement managed `.gitignore`, migration, corruption handling, and `--no-gitignore`; add acceptance tests.
  - Verify: focused pytest gate.
  - Gate: quick.

## Phase 3 — Documentation

- [ ] T3 Update README/help and self-hosting policy.
  - Verify: focused strings/help tests and skillgen check.
  - Gate: build.

## Phase 4 — Validation

- [ ] T4 Run full gate, standalone fresh-eyes validation, graph refresh, and record evidence.
  - Verify: full suite baseline and discrimination sensor.
  - Gate: build.

## Gate Check Commands

- Quick: `pytest -q tests/test_agents_platform.py tests/test_install.py tests/test_install_upgrade.py tests/test_install_strings.py`
- Build: `.venv/bin/python -m tools.skillgen --check && pytest -q`
