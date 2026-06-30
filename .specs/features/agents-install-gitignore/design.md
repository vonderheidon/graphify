# Design

Keep `.gitignore` ownership in `graphify.__main__`, next to the native
`agents`/`skills` install orchestration. A small pure renderer validates marker
shape, removes only exact managed legacy lines, and inserts/replaces one
canonical block. The install flow catches marker errors so agent integration
continues while the unsafe `.gitignore` write is skipped.

Only the friendly `agents` and `skills` subcommands manage `.gitignore`.
Platform-specific installs and generic `--platform agents` remain unchanged.
