# #0008 The GRS-03 router coverage test checks build intent and build.md independently, so deleting the primary command-table association survives while incidental build.md mentions remain.

- 2026-06-30T11:51:48Z `issue`: The GRS-03 router coverage test checks build intent and build.md independently, so deleting the primary command-table association survives while incidental build.md mentions remain. [tests/test_skillgen.py:413]
- 2026-06-30T11:52:55Z `attempt`: Added an exact primary-build router-row contract; Quick gate passed 65 tests and the prior scratch mutation now fails the GRS-03 route test. [tests/test_skillgen.py:101] (worked)
- 2026-06-30T11:53:01Z `fix`: GRS-03 now requires the build intents and references/build.md target in the same command-router row; the verifier's surviving mutation is killed. [tests/test_skillgen.py:101]
