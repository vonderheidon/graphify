## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, invoke the `skill` tool with `skill: "graphify"` before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

<!-- >>> projectmem agents bridge >>> -->
## ProjectMem

Use the smallest sufficient context layer:
- **short** — `pjm brief` / `get_summary()` for orientation.
- **focused** — `pjm context [--focus PATH]` / `get_context()` for scoped work.
- **complete** — `pjm instructions`, `pjm show`, and `pjm map` / `get_instructions()`, `get_summary()`, and `get_project_map()`.

Before mutating files or project memory, load the complete layer and run `pjm precheck --working` (or `precheck_file(path)`). Log issues, attempts, fixes, decisions, and notes through ProjectMem MCP tools or `pjm log`, `pjm attempt`, `pjm fix`, `pjm decision`, and `pjm note`. Never edit `.projectmem/summary.md` or `.projectmem/events.jsonl` directly.
<!-- <<< projectmem agents bridge <<< -->
