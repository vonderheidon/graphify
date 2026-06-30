# #0012 graphify agents install consumes the opening ProjectMem bridge marker placed between the Graphify section and the next H2, leaving an incomplete marker pair that pjm init correctly refuses to update.

- 2026-06-30T20:51:41Z `issue`: graphify agents install consumes the opening ProjectMem bridge marker placed between the Graphify section and the next H2, leaving an incomplete marker pair that pjm init correctly refuses to update. [graphify/__main__.py:1598; AGENTS.md]
- 2026-06-30T20:55:08Z `attempt`: Preserved HTML bridge markers immediately before the next H2 when replacing an unmarked Graphify section; 115 focused tests, skillgen, and 2548 full tests passed. [graphify/__main__.py:598; tests/test_agents_platform.py] (worked)
- 2026-06-30T20:55:08Z `fix`: Graphify AGENTS upgrades now retain the following ProjectMem opening marker, preventing incomplete bridge pairs during sequential bootstrap. [graphify/__main__.py:598]
