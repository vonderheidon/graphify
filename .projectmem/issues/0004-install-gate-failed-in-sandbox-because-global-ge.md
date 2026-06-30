# #0004 Install gate failed in sandbox because global Gemini/Vscode install tests wrote under read-only /home/jefferson; rerun with HOME in /tmp for this environment.

- 2026-06-30T11:09:12Z `issue`: Install gate failed in sandbox because global Gemini/Vscode install tests wrote under read-only /home/jefferson; rerun with HOME in /tmp for this environment. [tests/test_install.py:844]
- 2026-06-30T11:09:29Z `attempt`: Reran install gate with HOME=/tmp/graphify-test-home and UV_CACHE_DIR=/tmp/uv-cache; sandbox-only read-only HOME failure disappeared. [tests/test_install.py:844] (worked)
- 2026-06-30T11:09:29Z `fix`: Install gate is valid in this sandbox when HOME and UV cache point to writable /tmp; no product code change needed. [tests/test_install.py:844]
