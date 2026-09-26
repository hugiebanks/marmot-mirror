#!/usr/bin/env python3
"""Quickly check a Discord interaction fixture from the command line."""

import json
import sys
from pathlib import Path


def lint(value):
    issues = []
    if not isinstance(value, dict):
        return ["top-level JSON value should be an object"]

    if value.get("type") not in (1, 2, 3, 4, 5):
        issues.append("type should be 1 (ping) or 2–5 (interaction)")
    if not isinstance(value.get("token"), str) or not value["token"]:
        issues.append("token is missing or not a string")
    if value.get("version") != 1:
        issues.append("version is usually 1")
    if not value.get("application_id"):
        issues.append("application_id is missing")

    kind = value.get("type")
    data = value.get("data")
    if kind in (2, 4):
        if not isinstance(data, dict):
            issues.append("this interaction type usually has a data object")
        elif not isinstance(data.get("name"), str):
            issues.append("data.name is missing")
    if kind in (3, 5) and (not isinstance(data, dict) or not data.get("custom_id")):
        issues.append("component and modal submits need data.custom_id")
    if (value.get("guild_id") or value.get("channel_id")) and not value.get("member") and not value.get("user"):
        issues.append("server interactions usually include member or user")
    return issues


def main():
    if len(sys.argv) != 2:
        print("usage: python fixture_lint.py interaction.json", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except OSError as error:
        print(f"can't read {path}: {error}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as error:
        print(f"invalid JSON at line {error.lineno}, column {error.colno}: {error.msg}", file=sys.stderr)
        return 1

    issues = lint(payload)
    if issues:
        print(f"{path}: {len(issues)} thing(s) to check")
        for issue in issues:
            print(f"  - {issue}")
        return 1

    print(f"{path}: interaction envelope looks good")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
