#!/usr/bin/env python3
"""List SHARCNET Brine models, then ask the Gemma model a question."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def api_request(method: str, path: str, payload: dict | None = None) -> dict:
    base_url = os.environ["BRINE_BASE_URL"].rstrip("/")
    body = None if payload is None else json.dumps(payload).encode("utf-8")
    request = Request(
        f"{base_url}{path}",
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {os.environ['BRINE_API_KEY']}",
            "Content-Type": "application/json",
        },
    )

    try:
        with urlopen(request, timeout=120) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Request failed: {exc.reason}") from exc


def main() -> int:
    repo_dir = Path(__file__).resolve().parents[1]
    load_dotenv(repo_dir / ".env")

    missing = [name for name in ("BRINE_BASE_URL", "BRINE_API_KEY") if not os.environ.get(name)]
    if missing:
        print(f"Missing required environment variable(s): {', '.join(missing)}", file=sys.stderr)
        print("Copy .env.example to .env or export the variables in your shell.", file=sys.stderr)
        return 2

    model = os.environ.get("BRINE_MODEL", "gemma-4-31B-it")

    print("== Listing models ==")
    models = api_request("GET", "/models")
    print(json.dumps(models, indent=2))

    print(f"\n== Asking {model} ==")
    completion = api_request(
        "POST",
        "/chat/completions",
        {
            "model": model,
            "messages": [
                {
                    "role": "user",
                    "content": "In two sentences, explain what SHARCNET Brine is useful for.",
                }
            ],
            "temperature": 0.2,
            "max_tokens": 200,
        },
    )
    print(completion["choices"][0]["message"]["content"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
