#!/usr/bin/env python3
"""版本一致性门禁（mcp/ 子目录 + 双清单形态）。

为什么要有这个：2026-11-15 出过 `__version__` 字面量跟着新版本一起发布的漂移事故，
装到新版本却报旧版本，而当时的验收矩阵把它记成"一致"；同日又在 reg-hub 发现
`server.json`（仓库根，发布用）与 `mcp/server.json`（副本）版本各说各话。
这个门禁把两类缺陷都变成构建期红叉：

1. pyproject.toml 的 version；
2. 存在即检查的每一份 server.json（仓库根与 mcp/）的 version 与 packages[].version；
3. 安装后 importlib.metadata 报出的版本。

用法（CI 里先装包再跑本脚本，工作目录 mcp/）：
    python -m pip install .
    python tools/version_gate.py
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent  # mcp/


def pyproject_version() -> str:
    txt = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    m = re.search(r'^version\s*=\s*"([^"]+)"', txt, re.M)
    if m:
        return m.group(1)
    m = re.search(r'^version\s*=\s*\{.*?attr\s*=\s*"([^"]+)"', txt, re.M)
    if m:
        return "attr:" + m.group(1)
    raise SystemExit("GATE FAIL: pyproject.toml 里找不到 version")


def dist_name() -> str | None:
    txt = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    m = re.search(r'^name\s*=\s*"([^"]+)"', txt, re.M)
    return m.group(1) if m else None


def manifests() -> list[pathlib.Path]:
    found = []
    for p in (ROOT / "server.json", ROOT.parent / "server.json"):
        if p.exists():
            found.append(p)
    return found


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--static-only", action="store_true")
    a = ap.parse_args()

    pv = pyproject_version()
    checks: list[tuple[str, str]] = [("pyproject.toml", pv)]

    ms = manifests()
    if not ms:
        print("GATE FAIL: 找不到任何 server.json")
        return 1
    for mp in ms:
        d = json.loads(mp.read_text(encoding="utf-8"))
        checks.append((f"{mp.parent.name}/{mp.name} version", d.get("version", "")))
        for pkg in d.get("packages") or []:
            checks.append((f"{mp.parent.name}/{mp.name} packages[{pkg.get('identifier')}]", pkg.get("version", "")))

    if not pv.startswith("attr:") and not a.static_only and dist_name():
        try:
            from importlib.metadata import version as v
            checks.append((f"runtime {dist_name()}", v(dist_name())))
        except Exception as e:
            checks.append((f"runtime {dist_name()} (unavailable)", f"<{type(e).__name__}>"))

    problems = []
    for label, value in checks[1:]:
        if not value or value.startswith("<"):
            problems.append(f"{label}: 取不到值（{value!r}）")
        elif value != pv:
            problems.append(f"{label}: {value} != {pv}（pyproject.toml）")

    for label, value in checks:
        print(f"  {label:<52} {value or '<empty>'}")
    if problems:
        print("\nGATE FAIL:")
        for p in problems:
            print("  - " + p)
        return 1
    print("\nGATE PASS: 版本来源一致（含全部清单副本）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
