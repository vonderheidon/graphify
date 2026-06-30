# #0010 graphify skills --help is intercepted by the global help shortcut and prints only the generic hint, so the new command-specific lifecycle help is unreachable.

- 2026-06-30T20:29:12Z `issue`: graphify skills --help is intercepted by the global help shortcut and prints only the generic hint, so the new command-specific lifecycle help is unreachable. [graphify/__main__.py]
- 2026-06-30T20:29:12Z `attempt`: Added help handling inside the agents/skills command branch; focused tests showed that the earlier global --help shortcut wins before that branch. [graphify/__main__.py] (failed)
- 2026-06-30T20:29:43Z `attempt`: Excluded agents/skills from the generic nested-help shortcut so their branch renders lifecycle help; 114 focused tests and all 148 skillgen artifacts passed. [graphify/__main__.py] (worked)
- 2026-06-30T20:29:43Z `fix`: agents/skills command-specific help is now reachable and documents --no-gitignore plus uninstall retention. [graphify/__main__.py]
