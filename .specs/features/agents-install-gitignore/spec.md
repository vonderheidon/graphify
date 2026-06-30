# Agents Install Gitignore

## Requirements

- **GIG-01**: `graphify agents install` and `graphify skills install` create or update a delimited Graphify block in `.gitignore`.
- **GIG-02**: the block ignores local cache, cost, interpreter/root, vocabulary, temporary, conversion, and dated snapshot artifacts while keeping shared graph, report, manifest, labels, memory, and reflections versionable.
- **GIG-03**: exact broad rules `graphify-out/` and `/graphify-out/`, plus equivalent managed granular rules, migrate into the block without duplication; unrelated user rules remain byte-stable.
- **GIG-04**: repeated installation is byte-idempotent and an existing valid block is replaced in place.
- **GIG-05**: incomplete or corrupt managed markers preserve `.gitignore`, report an explicit error, and do not prevent skill/AGENTS installation.
- **GIG-06**: `--no-gitignore` leaves `.gitignore` byte-identical.
- **GIG-07**: uninstall removes agent integration but retains the managed `.gitignore` block.

## Edge cases

- Missing and empty `.gitignore`.
- Existing user content with and without a final newline.
- Manual granular Graphify rules mixed with unrelated rules.
- `.graphify_labels.json` must remain versionable.
- A start marker without an end marker, an end marker without a start marker, or reversed markers.

## Gates

- Focused: `pytest -q tests/test_agents_platform.py tests/test_install.py tests/test_install_upgrade.py tests/test_install_strings.py`
- Skill generation: `.venv/bin/python -m tools.skillgen --check`
- Full: isolated `HOME` and cache, baseline at least 2541 passing with the three known skips.
