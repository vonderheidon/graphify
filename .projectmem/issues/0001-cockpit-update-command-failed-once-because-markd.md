# #0001 Cockpit update command failed once because markdown backticks were expanded by the shell inside a double-quoted python -c payload.

- 2026-06-30T04:34:24Z `issue`: Cockpit update command failed once because markdown backticks were expanded by the shell inside a double-quoted python -c payload. [/home/jefferson/Dev/projetos/geral/handoffs/context-optimization/00-cockpit.md]
- 2026-06-30T04:34:30Z `attempt`: Retried cockpit update with single-quoted python payload so markdown backticks stayed literal. [/home/jefferson/Dev/projetos/geral/handoffs/context-optimization/00-cockpit.md] (worked)
- 2026-06-30T04:34:30Z `fix`: Cockpit update completed after quoting-safe retry; no further action needed for issue #0001. [/home/jefferson/Dev/projetos/geral/handoffs/context-optimization/00-cockpit.md]
