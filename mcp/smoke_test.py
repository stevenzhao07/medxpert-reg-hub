# -*- coding: utf-8 -*-
"""本地冒烟测试 medxpert MCP 工具（直接调用函数，不经 stdio）。"""
import io, sys, os, json
sys.path.insert(0, r"D:\Workbuddy\08-理论体系\发布\技能治理\medxpert-mcp")
import server

out = []
try:
    r = json.loads(server.udi_lookup(product_name="他克莫司"))
    out.append("udi_lookup 他克莫司: total=%d first=%s" % (r["total"], r["items"][0]["udi_main"] if r["items"] else "-"))
except Exception as e:
    out.append("udi_lookup FAIL: %s" % e)
try:
    r = json.loads(server.fda_510k_lookup(k_number="K234042"))
    out.append("510k K234042: total=%d id=%s" % (r["total"], r["items"][0]["k_number"] if r["items"] else "-"))
except Exception as e:
    out.append("510k FAIL: %s" % e)
try:
    r = json.loads(server.class_lookup(product_code="HRX"))
    out.append("class HRX: total=%d" % r["total"])
except Exception as e:
    out.append("class FAIL: %s" % e)
try:
    r = json.loads(server.hub_search("关节镜"))
    out.append("hub_search 关节镜: total=%d top_files=%s" % (r["total"], sorted({h["file"] for h in r["top"]})[:3]))
except Exception as e:
    out.append("hub_search FAIL: %s" % e)

io.open(r"D:\Workbuddy\08-理论体系\发布\技能治理\medxpert-mcp\smoke_test.log", "w", encoding="utf-8").write("\n".join(out))
