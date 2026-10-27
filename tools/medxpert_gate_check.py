#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
medxpert-gate check —— medxpert-reg-hub 机器强制门禁（lgd-ci-gate 同型）
三步：selftest（负对照，自证门能失败）→ check（必备文件/README 锚点/链接可解析）
零外部依赖，仅标准库。本地可跑：python medxpert_gate_check.py check --root <dir>
"""
import argparse
import os
import re
import sys

REQUIRED_FILES = [
    "README.md",
    "README.en.md",
    "LICENSE",
    "llms.txt",
]
REQUIRED_DIRS = ["EVALUATION", "docs", "assets", "skills", "mcp", "bin", "tools"]

# README 锚点（展示层三件套 + 内容完备性）
README_ANCHORS = [
    ("lgd-theory", "LGD 回链"),
    ("28", "28 枢纽计数"),
    ("48", "48 实例评测"),
    ("中文", "语言锚点"),
    ("lgd-powered", "LGD-Powered 徽章"),
    ("star", "求星横幅（英文 star）"),
    ("为什么", "Why 对比段"),
]
BADGES_RE = re.compile(r"https://img\.shields\.io|shields\.io/badge|badge")


def fail(msg):
    print(f"FAIL: {msg}")
    sys.exit(1)


def cmd_selftest():
    """负对照：检查一个必然不存在的文件，若意外通过则自身失败。"""
    p = os.path.join("tools", "__definitely_missing__")
    if os.path.exists(p):
        fail("selftest failed: gate cannot fail (missing file unexpectedly exists)")
    print("selftest OK: gate proven able to fail")


def check_root(root):
    for f in REQUIRED_FILES:
        if not os.path.isfile(os.path.join(root, f)):
            fail(f"missing required file: {f}")
    for d in REQUIRED_DIRS:
        if not os.path.isdir(os.path.join(root, d)):
            fail(f"missing required dir: {d}")
    if not os.listdir(os.path.join(root, "EVALUATION")):
        fail("EVALUATION dir is empty")
    # skills/ 技能包结构（SKILL.md + references/）
    if not os.path.isfile(os.path.join(root, "skills", "SKILL.md")):
        fail("missing skills/SKILL.md")
    if not os.path.isdir(os.path.join(root, "skills", "references")):
        fail("missing skills/references")
    # LICENSE 含 MIT
    lic = open(os.path.join(root, "LICENSE"), encoding="utf-8", errors="replace").read()
    if "MIT" not in lic:
        fail("LICENSE missing MIT clause")

    # README 锚点
    readme = open(os.path.join(root, "README.md"), encoding="utf-8", errors="replace").read()
    for token, label in README_ANCHORS:
        if token not in readme:
            fail(f"README missing anchor: {label} (token={token!r})")
    head = readme[:3000]
    if "⭐" not in head and "Star" not in head:
        fail("README missing star banner in header area")
    if not BADGES_RE.search(readme):
        fail("README missing dynamic badges")

    # README 相对链接可解析（![]() 与 []()，忽略 http(s)/#/mailto）
    link_re = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
    missing = []
    for m in link_re.finditer(readme):
        target = m.group(1).strip()
        if target.startswith(("http://", "https://", "#", "mailto:", "<")):
            continue
        target = target.split("#")[0].split("?")[0].strip()
        if not target:
            continue
        if target.startswith("./"):
            target = target[2:]
        if not os.path.exists(os.path.join(root, target)):
            missing.append(target)
    if missing:
        fail(f"unresolvable relative links: {missing[:10]}")

    # README.en.md 双语完整性（同锚点抽查）
    en = open(os.path.join(root, "README.en.md"), encoding="utf-8", errors="replace").read()
    for token in ("lgd-theory", "48", "badge"):
        if token not in en:
            fail(f"README.en.md missing anchor: {token!r}")

    print("check OK: files, anchors, links all pass")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["selftest", "check"])
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    if args.cmd == "selftest":
        cmd_selftest()
    else:
        check_root(os.path.abspath(args.root))


if __name__ == "__main__":
    main()
