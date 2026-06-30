# #0007 The full pytest gate hangs at tests/test_serve_http.py::test_app_builds_and_initialize_succeeds under the restricted sandbox; the HTTP block passes outside it, so final validation must allow local TestClient binding.

- 2026-06-30T11:38:19Z `issue`: The full pytest gate hangs at tests/test_serve_http.py::test_app_builds_and_initialize_succeeds under the restricted sandbox; the HTTP block passes outside it, so final validation must allow local TestClient binding. [tests/test_serve_http.py:24]
- 2026-06-30T11:39:24Z `attempt`: Re-ran the full pytest gate with local TestClient binding permitted; all 2541 tests passed with 3 intentional skips. [tests/test_serve_http.py:24] (worked)
- 2026-06-30T11:39:27Z `fix`: Final test execution profile now permits the local HTTP binding required by TestClient; full gate passes 2541/2541 with 3 skips. [tests/test_serve_http.py:24]
