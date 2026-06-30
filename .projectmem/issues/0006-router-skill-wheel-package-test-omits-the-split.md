# #0006 Router skill wheel package test omits the split agents host from _SPLIT_HOSTS, so GRS-05 all split-platform references is not fully proven.

- 2026-06-30T11:27:20Z `issue`: Router skill wheel package test omits the split agents host from _SPLIT_HOSTS, so GRS-05 all split-platform references is not fully proven. [tests/test_install_references.py:375]
- 2026-06-30T11:31:41Z `attempt`: Expanded the wheel payload regression guard to include skill-agents.md and all 9 agents references; the focused wheel test passed. [tests/test_install_references.py:356] (worked)
- 2026-06-30T11:31:44Z `fix`: Wheel payload verification now covers 16 skill bodies and 126 references across all 14 split hosts, including agents. [tests/test_install_references.py:356]
