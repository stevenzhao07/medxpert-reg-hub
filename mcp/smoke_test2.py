# -*- coding: utf-8 -*-
"""冒烟测试 v2：含 json_extract 修正后的 510k/class 查询。"""
import io, sys, json
sys.path.insert(0, r"D:\Workbuddy\08-理论体系\发布\技能治理\medxpert-mcp")
import server

out = []
r = json.loads(server.udi_lookup(di="06977181060182"))
out.append("udi_lookup DI: total=%d product=%s" % (r["total"], r["items"][0]["product_name"] if r["items"] else "-"))
r = json.loads(server.fda_510k_lookup(company="Diagnostic"))
out.append("510k company=Diagnostic: total=%d first=%s" % (r["total"], r["items"][0]["k_number"] if r["items"] else "-"))
r = json.loads(server.fda_510k_lookup(product="Sterilization"))
out.append("510k product=Sterilization: total=%d" % r["total"])
r = json.loads(server.class_lookup(product_code="HRX"))
out.append("class HRX: total=%d first=%s" % (r["total"], r["items"][0]["device_name"] if r["items"] else "-"))
r = json.loads(server.class_lookup(product_name="Arthroscope"))
out.append("class Arthroscope: total=%d" % r["total"])
r = json.loads(server.pma_lookup(company="Medtronic"))
out.append("pma Medtronic: total=%d" % r["total"])
io.open(r"D:\Workbuddy\08-理论体系\发布\技能治理\medxpert-mcp\smoke_test2.log", "w", encoding="utf-8").write("\n".join(out))
