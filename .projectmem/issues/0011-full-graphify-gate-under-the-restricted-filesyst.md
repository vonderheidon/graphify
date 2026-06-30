# #0011 Full Graphify gate under the restricted filesystem produced write-related failures and hung at tests/test_serve_http.py before completion; this environment cannot host the full suite.

- 2026-06-30T20:40:24Z `issue`: Full Graphify gate under the restricted filesystem produced write-related failures and hung at tests/test_serve_http.py before completion; this environment cannot host the full suite. [tests/test_serve_http.py; test environment]
- 2026-06-30T20:40:24Z `attempt`: Ran 2550-test suite in sandbox with isolated HOME/cache; write-dependent tests failed and execution hung at the HTTP block, then was interrupted. [test environment] (failed)
- 2026-06-30T20:42:50Z `attempt`: Reran the complete Graphify gate outside the sandbox with isolated HOME/cache; 2547 passed and 3 known tests skipped. [test environment] (worked)
- 2026-06-30T20:42:50Z `fix`: Full Graphify validation profile passes outside the restricted filesystem and local HTTP sandbox: 2547 passed, 3 skipped. [test environment]
