"""OpenCode Go global credential resolution and security policy."""

import json
import os
from pathlib import Path
from unittest.mock import patch

import pytest

from graphify import llm


def _auth_path(tmp_path: Path, monkeypatch, *, payload=None, mode=0o600) -> Path:
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path))
    path = tmp_path / "opencode" / "auth.json"
    path.parent.mkdir(parents=True)
    data = payload or {"opencode-go": {"type": "api", "key": "stored-secret"}}
    path.write_text(json.dumps(data), encoding="utf-8")
    path.chmod(mode)
    return path


def _clear_provider_env(monkeypatch) -> None:
    for name in (
        "OPENCODE_GO_API_KEY",
        "GEMINI_API_KEY",
        "GOOGLE_API_KEY",
        "MOONSHOT_API_KEY",
        "ANTHROPIC_API_KEY",
        "OPENAI_API_KEY",
        "DEEPSEEK_API_KEY",
        "OLLAMA_BASE_URL",
        "AWS_PROFILE",
        "AWS_REGION",
        "AWS_DEFAULT_REGION",
    ):
        monkeypatch.delenv(name, raising=False)


def test_global_auth_is_resolved_from_xdg_independent_of_cwd(tmp_path, monkeypatch):
    _clear_provider_env(monkeypatch)
    _auth_path(tmp_path, monkeypatch)
    elsewhere = tmp_path / "unrelated" / "repo"
    elsewhere.mkdir(parents=True)

    monkeypatch.chdir(elsewhere)

    assert llm._get_backend_api_key("opencode-go") == "stored-secret"
    assert llm.detect_backend() == "opencode-go"


def test_global_auth_falls_back_to_home_local_share(tmp_path, monkeypatch):
    _clear_provider_env(monkeypatch)
    monkeypatch.delenv("XDG_DATA_HOME", raising=False)
    monkeypatch.setenv("HOME", str(tmp_path))
    path = tmp_path / ".local" / "share" / "opencode" / "auth.json"
    path.parent.mkdir(parents=True)
    path.write_text(
        json.dumps({"opencode-go": {"type": "api", "key": "home-secret"}}),
        encoding="utf-8",
    )
    path.chmod(0o600)

    assert llm._get_backend_api_key("opencode-go") == "home-secret"


def test_env_key_precedes_global_auth(tmp_path, monkeypatch):
    _clear_provider_env(monkeypatch)
    _auth_path(tmp_path, monkeypatch)
    monkeypatch.setenv("OPENCODE_GO_API_KEY", "environment-secret")

    assert llm._get_backend_api_key("opencode-go") == "environment-secret"


def test_explicit_key_precedes_env_and_global_auth(tmp_path, monkeypatch):
    _clear_provider_env(monkeypatch)
    _auth_path(tmp_path, monkeypatch)
    monkeypatch.setenv("OPENCODE_GO_API_KEY", "environment-secret")
    source = tmp_path / "note.md"
    source.write_text("# Note\n", encoding="utf-8")
    result = {
        "nodes": [],
        "edges": [],
        "hyperedges": [],
        "input_tokens": 1,
        "output_tokens": 1,
    }

    with patch("graphify.llm._call_openai_compat", return_value=result) as call:
        llm.extract_files_direct(
            [source],
            backend="opencode-go",
            api_key="explicit-secret",
            root=tmp_path,
        )

    assert call.call_args.args[1] == "explicit-secret"


def test_autodetect_chooses_opencode_go_over_other_provider_keys(tmp_path, monkeypatch):
    _clear_provider_env(monkeypatch)
    _auth_path(tmp_path, monkeypatch)
    monkeypatch.setenv("GEMINI_API_KEY", "gemini-secret")
    monkeypatch.setenv("OPENAI_API_KEY", "openai-secret")

    assert llm.detect_backend() == "opencode-go"


def test_other_providers_are_not_auto_detected(tmp_path, monkeypatch):
    _clear_provider_env(monkeypatch)
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path))
    monkeypatch.setenv("GEMINI_API_KEY", "gemini-secret")
    monkeypatch.setenv("OPENAI_API_KEY", "openai-secret")

    assert llm.detect_backend() is None
    assert llm._get_backend_api_key("gemini") == "gemini-secret"


def test_missing_auth_gives_single_login_instruction(tmp_path, monkeypatch):
    _clear_provider_env(monkeypatch)
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path))

    with pytest.raises(ValueError) as exc:
        llm.extract_files_direct([tmp_path / "note.md"])

    message = str(exc.value)
    assert message.count("opencode auth login --provider opencode-go") == 1
    assert "OPENCODE_GO_API_KEY" in message


@pytest.mark.parametrize(
    "payload",
    [
        "{not-json",
        json.dumps({}),
        json.dumps({"opencode-go": {"type": "api", "key": ""}}),
        json.dumps({"opencode-go": {"type": "oauth", "key": "secret-value"}}),
    ],
)
def test_invalid_auth_fails_without_secret_leak(tmp_path, monkeypatch, payload):
    _clear_provider_env(monkeypatch)
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path))
    path = tmp_path / "opencode" / "auth.json"
    path.parent.mkdir(parents=True)
    path.write_text(payload, encoding="utf-8")
    path.chmod(0o600)

    with pytest.raises(ValueError) as exc:
        llm._get_backend_api_key("opencode-go")

    assert "secret-value" not in str(exc.value)


def test_symlink_auth_is_rejected_without_reading_target(tmp_path, monkeypatch):
    _clear_provider_env(monkeypatch)
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path / "data"))
    target = tmp_path / "target.json"
    target.write_text(
        json.dumps({"opencode-go": {"type": "api", "key": "symlink-secret"}}),
        encoding="utf-8",
    )
    target.chmod(0o600)
    path = tmp_path / "data" / "opencode" / "auth.json"
    path.parent.mkdir(parents=True)
    path.symlink_to(target)

    with pytest.raises(ValueError) as exc:
        llm._get_backend_api_key("opencode-go")

    assert "symlink-secret" not in str(exc.value)
    assert "non-symlink" in str(exc.value)


def test_open_permissions_are_rejected_without_secret_leak(tmp_path, monkeypatch):
    _clear_provider_env(monkeypatch)
    _auth_path(tmp_path, monkeypatch, mode=0o640)

    with pytest.raises(ValueError) as exc:
        llm._get_backend_api_key("opencode-go")

    assert "stored-secret" not in str(exc.value)
    assert "0600" in str(exc.value)


def test_wrong_owner_is_rejected_without_secret_leak(tmp_path, monkeypatch):
    _clear_provider_env(monkeypatch)
    _auth_path(tmp_path, monkeypatch)

    with patch("graphify.llm.os.getuid", return_value=os.getuid() + 1):
        with pytest.raises(ValueError) as exc:
            llm._get_backend_api_key("opencode-go")

    assert "stored-secret" not in str(exc.value)
    assert "current user" in str(exc.value)
