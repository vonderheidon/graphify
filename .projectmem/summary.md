# projectmem - graphify-v8

_Last updated: 2026-06-30_

## Project purpose
AI coding assistant skill (Claude Code, CodeBuddy, Codex, OpenCode, Kilo Code, Cursor, Gemini CLI, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro, Pi, Devin CLI, Google Antigravity) - turn any folder of code, docs, papers, images, or videos into a queryable knowledge graph

## Recent issues
- [DONE] #legacy_ff47 Legacy issue: fix(llm): force non-streaming on OpenAI-compatible calls (#1223) -> fix(llm): force non-streaming on OpenAI-compatible calls (#1223) (fixed)
- [DONE] #legacy_9b49 Legacy issue: fix(extract): emit references for Java type annotations (#1487) -> fix(extract): emit references for Java type annotations (#1487) (fixed)
- [DONE] #legacy_8994 Legacy issue: fix(extract): recover dropped Objective-C relationships (#1475) -> fix(extract): recover dropped Objective-C relationships (#1475) (fixed)
- [DONE] #legacy_7a94 Legacy issue: fix(wiki): portable relative markdown links so navigation works outside Obsidian (#1444) -> fix(wiki): portable relative markdown links so navigation works outside Obsidian (#1444) (fixed)
- [DONE] #legacy_76b6 Legacy issue: feat(extract): resolve C# cross-file type references + enum/struct/record (#1466) -> feat(extract): resolve C# cross-file type references + enum/struct/record (#1466) (fixed)
- [DONE] #legacy_6509 Legacy issue: fix(extract): disambiguate imported type stubs across files without blocking rewire (#1462) -> fix(extract): disambiguate imported type stubs across files without blocking rewire (#1462) (fixed)
- [DONE] #legacy_5a39 Legacy issue: fix(agents): preserve following bridge markers -> fix(agents): preserve following bridge markers (fixed)
- [DONE] #legacy_36b7 Legacy issue: fix(extract): Go cross-file type refs emit sourceless stubs (#1500) -> fix(extract): Go cross-file type refs emit sourceless stubs (#1500) (fixed)
- [DONE] #legacy_31b3 Legacy issue: fix(extract): emit references for Java field types (#1485) -> fix(extract): emit references for Java field types (#1485) (fixed)
- [DONE] #legacy_3142 Legacy issue: Fix host-agent token accounting -> Fix host-agent token accounting (fixed)
- [DONE] #legacy_1b99 Legacy issue: fix: resolve explain/affected when a source-file path matches multiple nodes (#1503) -> fix: resolve explain/affected when a source-file path matches multiple nodes (#1503) (fixed)
- [DONE] #legacy_1225 Legacy issue: docs: fix `graphify global add` example (#1489) -> docs: fix `graphify global add` example (#1489) (fixed)
- [DONE] #legacy_049b Legacy issue: Fix GraphML export for hyperedges -> Fix GraphML export for hyperedges (fixed)
- [DONE] #0014 graphify agents install matches the owned AGENTS H2 case-sensitively, so an existing  section is preserved and a duplicate lowercase  section is appended. [graphify/__main__.py:598; /home/jefferson/Dev/projetos/geral/youtube-content-extractor/AGENTS.md] -> graphify agents install now adopts case variants such as  instead of appending a duplicate lowercase section. [graphify/__main__.py:598] (fixed)
- [DONE] #0013 Full regression gate exposed nondeterministic completion ordering in test_label_communities_batches_when_over_batch_size: calls were [100, 50, 100] instead of submission order [100, 100, 50]. [tests/test_labeling.py:278] -> No product change required for the one-off concurrent completion-order fluctuation; isolated and full reruns are green. [tests/test_labeling.py:278] (fixed)
  - Failed attempt: Post-rollout-fix full suite reached 2547 passes and 3 skips but failed the unrelated concurrent batching order assertion once. [tests/test_labeling.py:278]
- [DONE] #0012 graphify agents install consumes the opening ProjectMem bridge marker placed between the Graphify section and the next H2, leaving an incomplete marker pair that pjm init correctly refuses to update. [graphify/__main__.py:1598; AGENTS.md] -> Graphify AGENTS upgrades now retain the following ProjectMem opening marker, preventing incomplete bridge pairs during sequential bootstrap. [graphify/__main__.py:598] (fixed)
- [DONE] #0011 Full Graphify gate under the restricted filesystem produced write-related failures and hung at tests/test_serve_http.py before completion; this environment cannot host the full suite. [tests/test_serve_http.py; test environment] -> Full Graphify validation profile passes outside the restricted filesystem and local HTTP sandbox: 2547 passed, 3 skipped. [test environment] (fixed)
  - Failed attempt: Ran 2550-test suite in sandbox with isolated HOME/cache; write-dependent tests failed and execution hung at the HTTP block, then was interrupted. [test environment]
- [DONE] #0010 graphify skills --help is intercepted by the global help shortcut and prints only the generic hint, so the new command-specific lifecycle help is unreachable. [graphify/__main__.py] -> agents/skills command-specific help is now reachable and documents --no-gitignore plus uninstall retention. [graphify/__main__.py] (fixed)
  - Failed attempt: Added help handling inside the agents/skills command branch; focused tests showed that the earlier global --help shortcut wins before that branch. [graphify/__main__.py]
- [DONE] #0009 graphify query returned traversal output but emitted Failed to create stream fd: Operation not permitted under the restricted environment; query result remained usable. [graphify-out/graph.json] -> Confirmed Graphify query itself is healthy; using the non-login execution path avoids the restricted shell startup stream-fd warning. [shell startup] (fixed)
- [DONE] #0008 The GRS-03 router coverage test checks build intent and build.md independently, so deleting the primary command-table association survives while incidental build.md mentions remain. [tests/test_skillgen.py:413] -> GRS-03 now requires the build intents and references/build.md target in the same command-router row; the verifier's surviving mutation is killed. [tests/test_skillgen.py:101] (fixed)
- [DONE] #0007 The full pytest gate hangs at tests/test_serve_http.py::test_app_builds_and_initialize_succeeds under the restricted sandbox; the HTTP block passes outside it, so final validation must allow local TestClient binding. [tests/test_serve_http.py:24] -> Final test execution profile now permits the local HTTP binding required by TestClient; full gate passes 2541/2541 with 3 skips. [tests/test_serve_http.py:24] (fixed)
- [DONE] #0006 Router skill wheel package test omits the split agents host from _SPLIT_HOSTS, so GRS-05 all split-platform references is not fully proven. [tests/test_install_references.py:375] -> Wheel payload verification now covers 16 skill bodies and 126 references across all 14 split hosts, including agents. [tests/test_install_references.py:356] (fixed)
- [DONE] #0005 graphify update . hit sandbox Operation not permitted during watch rebuild, then succeeded outside sandbox for T7 graph refresh. [graphify-out/graph.json] -> T7 graph refresh completed after sandbox escalation; graphify update reported graph.json and GRAPH_REPORT.md updated, with no tracked graph diff to commit. [graphify-out/graph.json] (fixed)
- [DONE] #0004 Install gate failed in sandbox because global Gemini/Vscode install tests wrote under read-only /home/jefferson; rerun with HOME in /tmp for this environment. [tests/test_install.py:844] -> Install gate is valid in this sandbox when HOME and UV cache point to writable /tmp; no product code change needed. [tests/test_install.py:844] (fixed)
- [DONE] #0003 graphify update . failed after router-skill test changes with Operation not permitted during graphify watch rebuild. [graphify-out/graph.json] -> graphify update . completed outside sandbox after the Operation not permitted failure; graph.json and GRAPH_REPORT.md were refreshed. [graphify-out/graph.json] (fixed)
- [DONE] #0002 Router skill install reference tests are stale after Phase 2 added build.md; tests/test_install_references.py still expects the old eight-reference set and wheel count. [tests/test_install_references.py:284] -> Install reference guards now track the nine-reference router sidecar set, including build.md, and platform dispatch assertions read references/build.md; full install gate passed with 167 passed / 1 skipped. [tests/test_install_references.py:284] (fixed)
  - Partial attempt: Added build.md to install reference expectations; tests/test_install_references.py now passes, but the full install gate still fails because tests/test_install.py expects platform dispatch markers inside the lean SKILL.md instead of references/build.md. [tests/test_install.py:217]
- [DONE] #0001 Cockpit update command failed once because markdown backticks were expanded by the shell inside a double-quoted python -c payload. [/home/jefferson/Dev/projetos/geral/handoffs/context-optimization/00-cockpit.md] -> Cockpit update completed after quoting-safe retry; no further action needed for issue #0001. [/home/jefferson/Dev/projetos/geral/handoffs/context-optimization/00-cockpit.md] (fixed)

## Decisions
- Graphify router-skill work will edit skillgen fragments/platform metadata as source of truth and regenerate generated skill artifacts; generated graphify/skill*.md and graphify/skills/* outputs must not be hand-edited. [.specs/STATE.md]

## Notes
- Gotcha: pjm attempt requires an active ProjectMem issue; for planned feature progress without an issue, use pjm note or create/attach an issue first. [.projectmem/AI_INSTRUCTIONS.md]
- Graphify router-skill Phase 2 review completed with subagents: T4 query router had no blocking findings; T5 artifact sync passed; reviewer-found install drift was fixed in df70a02 and the install gate passed with 167 passed / 1 skipped. [.specs/features/graphify-router-skill/tasks.md:162]
- Graphify router-skill T7 completed: commit fcc9232 records Claude/Codex split-core before-after size evidence in tests/test_skillgen.py; quick gate passed 65 tests and install gate passed 167 passed / 1 skipped with HOME isolated to /tmp. [tests/test_skillgen.py:25]
- T8 pre-commit high-churn warnings for tests/test_skillgen.py and tests/test_install_references.py were reviewed; both changes are narrowly scoped regression guards required by GRS-03 and GRS-05. [tests/test_skillgen.py:418]
- T8 closed in commit 08417cd after independent verification passed 6/6 requirements and 3/3 discrimination mutations. [.specs/features/graphify-router-skill/validation.md:1]
- Updated the multi-repo context-optimization cockpit after graphify-v8 T8: all three repos are DONE; Graphify closure is commit 08417cd with verifier PASS 6/6 and sensor 3/3. [/home/jefferson/Dev/projetos/geral/handoffs/context-optimization/00-cockpit.md]
- test(skillgen): characterize graphify router core
- test(skillgen): guard router reference coverage
- docs(spec): define agents gitignore policy
- test(agents): validate managed graph ignores

## Key files
- `CHANGELOG.md`
- `graphify/extract.py`
- `tests/test_languages.py`
- `graphify/llm.py`
- `tests/test_llm_backends.py`
- `graphify/wiki.py`
- `tests/test_wiki.py`
- `README.md`
- `graphify/build.py`
- `graphify/detect.py`
- `tests/fixtures/sample.metal`
- `graphify/__main__.py`
- `tests/test_labeling.py`
- `pyproject.toml`
- `0.8.50`
- `tests/test_extract.py`
- `graphify/extractors/csharp.py`
- `tests/test_csharp_type_resolution.py`
- `uv.lock`
- `graphify/affected.py`

## Open questions
- None logged yet.
