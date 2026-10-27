# -*- coding: utf-8 -*-
"""medxpert-reg-hub MCP Server — 医疗器械注册合规数据查询（只读）。

工具（全部只读，连本地 SQLite 知识库）：
  - udi_lookup         NMPA UDI 查询（主DI/产品名/注册证号）629.5 万条
  - fda_510k_lookup    FDA 510(k) 查询（K 号/公司/产品）16.8 万条
  - pma_lookup         FDA PMA 查询（PMA 号/公司/产品）5.7 万条
  - class_lookup       FDA 产品分类查询（产品代码/名称）7,088 条
  - hub_search         20 大枢纽知识库关键词检索（中/美/欧/日分类与路径）

配置：
  env MEDXPERT_DB     SQLite 路径（默认 D:\\Workbuddy\\02-知识库\\MedXpert-RA-Data\\db\\medxpert_device.sqlite）
  env MEDXPERT_REFS   references 目录（默认 medxpert-reg-hub-npm\\skills\\references）

运行：python server.py   （stdio 模式；也可 uvicorn http 模式按需）
"""
import os
import json
import sqlite3
from mcp.server.mcpserver import MCPServer

DEFAULT_DB = r"D:\Workbuddy\02-知识库\MedXpert-RA-Data\db\medxpert_device.sqlite"
DEFAULT_REFS = r"D:\Workbuddy\08-理论体系\发布\技能治理\medxpert-reg-hub-npm\skills\references"

DB = os.environ.get("MEDXPERT_DB", DEFAULT_DB)
REFS = os.environ.get("MEDXPERT_REFS", DEFAULT_REFS)

mcp = MCPServer("medxpert-reg-hub", instructions="医疗器械全球注册合规数据查询：NMPA UDI、FDA 510(k)/PMA/分类、枢纽知识库速查。只读。")

_MAX = 20


def _conn():
    return sqlite3.connect(DB, timeout=30)


def _like_rows(table, field, q, limit=_MAX, keys=("id", "payload")):
    conn = _conn()
    try:
        cur = conn.execute(
            "SELECT id, payload FROM %s WHERE %s LIKE ? LIMIT ?" % (table, field),
            ("%" + q + "%", limit),
        )
        rows = [{"id": r[0], "payload": (r[1] or "")[:400]} for r in cur.fetchall()]
        return rows
    finally:
        conn.close()


@mcp.tool()
def udi_lookup(di: str = "", product_name: str = "", reg_no: str = "") -> str:
    """NMPA 医疗器械唯一标识（UDI）查询：按 主DI 精确查，或按 产品名称/注册证号 模糊查。返回最多 20 条。
    字段：udi_main 主DI、product_name 产品名称、spec 规格、reg_no 注册证号、regrant_name 注册人、class_code 分类编码、device_class 类别、issue_date 发码日期。
    """
    conn = _conn()
    try:
        if di:
            cur = conn.execute(
                "SELECT udi_main, product_name, spec, class_code, device_class, reg_no, regrant_name, issue_date "
                "FROM nmpa_udi WHERE udi_main=? LIMIT ?", (di, _MAX))
        else:
            kw = product_name or reg_no
            if not kw:
                return json.dumps({"error": "请提供 di、product_name 或 reg_no"}, ensure_ascii=False)
            field = "product_name" if product_name else "reg_no"
            cur = conn.execute(
                "SELECT udi_main, product_name, spec, class_code, device_class, reg_no, regrant_name, issue_date "
                "FROM nmpa_udi WHERE %s LIKE ? LIMIT ?" % field, ("%" + kw + "%", _MAX))
        rows = [dict(zip(["udi_main", "product_name", "spec", "class_code", "device_class", "reg_no", "regrant_name", "issue_date"], r))
                for r in cur.fetchall()]
        return json.dumps({"total": len(rows), "items": rows}, ensure_ascii=False)
    finally:
        conn.close()


@mcp.tool()
def fda_510k_lookup(k_number: str = "", company: str = "", product: str = "") -> str:
    """FDA 510(k) 数据库查询：按 K 号精确（如 K234042），或按 公司/applicant、产品名 模糊。返回最多 10 条。
    """
    conn = _conn()
    try:
        if k_number:
            cur = conn.execute(
                "SELECT json_extract(payload,'$.k_number') k, json_extract(payload,'$.applicant') applicant, "
                "json_extract(payload,'$.openfda.device_name') name, json_extract(payload,'$.product_code') pc "
                "FROM device_510k WHERE json_extract(payload,'$.k_number')=? LIMIT ?", (k_number, 10))
        else:
            kw = company or product
            if not kw:
                return json.dumps({"error": "请提供 k_number、company 或 product"}, ensure_ascii=False)
            field = "json_extract(payload,'$.applicant')" if company else "json_extract(payload,'$.openfda.device_name')"
            cur = conn.execute(
                "SELECT json_extract(payload,'$.k_number') k, json_extract(payload,'$.applicant') applicant, "
                "json_extract(payload,'$.openfda.device_name') name, json_extract(payload,'$.product_code') pc "
                "FROM device_510k WHERE %s LIKE ? LIMIT ?" % field, ("%" + kw + "%", 10))
        rows = [{"k_number": r[0], "applicant": r[1], "device_name": r[2], "product_code": r[3]} for r in cur.fetchall()]
        return json.dumps({"total": len(rows), "items": rows}, ensure_ascii=False)
    finally:
        conn.close()


@mcp.tool()
def pma_lookup(pma_number: str = "", company: str = "", product: str = "") -> str:
    """FDA PMA（上市前批准）查询：按 PMA 号（如 P980016）、公司或产品模糊。返回最多 10 条。
    """
    conn = _conn()
    try:
        if pma_number:
            cur = conn.execute("SELECT id, payload FROM device_pma WHERE id LIKE ? LIMIT ?", ("%" + pma_number + "%", 10))
        else:
            kw = company or product
            if not kw:
                return json.dumps({"error": "请提供 pma_number、company 或 product"}, ensure_ascii=False)
            cur = conn.execute("SELECT id, payload FROM device_pma WHERE payload LIKE ? LIMIT ?", ("%" + kw + "%", 10))
        rows = [{"pma_number": r[0], "detail": (r[1] or "")[:400]} for r in cur.fetchall()]
        return json.dumps({"total": len(rows), "items": rows}, ensure_ascii=False)
    finally:
        conn.close()


@mcp.tool()
def class_lookup(product_code: str = "", product_name: str = "") -> str:
    """FDA 医疗器械产品分类查询（21 CFR 分类 7,088 条）：按 产品代码（如 HRX）或 产品名称/device_name。返回最多 10 条。
    """
    conn = _conn()
    try:
        if product_code:
            cur = conn.execute(
                "SELECT json_extract(payload,'$.product_code') pc, json_extract(payload,'$.device_name') name, "
                "json_extract(payload,'$.medical_specialty_description') spec, json_extract(payload,'$.regulation_number') reg "
                "FROM device_classification WHERE json_extract(payload,'$.product_code')=? LIMIT ?",
                (product_code.upper(), 10))
        else:
            if not product_name:
                return json.dumps({"error": "请提供 product_code 或 product_name"}, ensure_ascii=False)
            cur = conn.execute(
                "SELECT json_extract(payload,'$.product_code') pc, json_extract(payload,'$.device_name') name, "
                "json_extract(payload,'$.medical_specialty_description') spec, json_extract(payload,'$.regulation_number') reg "
                "FROM device_classification WHERE json_extract(payload,'$.device_name') LIKE ? LIMIT ?",
                ("%" + product_name + "%", 10))
        rows = [{"product_code": r[0], "device_name": r[1], "specialty": r[2], "regulation": r[3]} for r in cur.fetchall()]
        return json.dumps({"total": len(rows), "items": rows}, ensure_ascii=False)
    finally:
        conn.close()


@mcp.tool()
def hub_search(keyword: str) -> str:
    """医械注册枢纽知识库关键词检索：跨 20 大枢纽（注册工程师资料/UDI/STED/GMP/临床评价/上市后监管/市场准入等）检索产品分类与注册路径要点，返回命中文件、行号与上下文。适合"某产品在X国怎么注册"类问题。
    """
    if not keyword or not os.path.isdir(REFS):
        return json.dumps({"error": "需要 keyword 且 references 目录存在"}, ensure_ascii=False)
    kw = keyword.lower()
    hits = []
    for f in sorted(os.listdir(REFS)):
        if not f.endswith(".md"):
            continue
        p = os.path.join(REFS, f)
        for i, line in enumerate(open(p, encoding="utf-8"), 1):
            if kw in line.lower():
                hits.append({"file": f, "line": i, "text": line.strip()[:160]})
    top = hits[:10]
    return json.dumps({"total": len(hits), "top": top}, ensure_ascii=False)


def main():
    """Console entry point (stdio MCP server)."""
    mcp.run()


if __name__ == "__main__":
    main()
