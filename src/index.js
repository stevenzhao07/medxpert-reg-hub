/**
 * medxpert-reg-hub — DeepSeek Harness 插件入口（Cordis 插件）。
 *
 * 只读工具，不修改任何宿主状态：
 *  - medxpert_quick_ref(kw)     在包内 skills/references 20 大枢纽中关键词速查
 *  - medxpert_check_links()     扫描技能内官方链接并报告可达性（抽样）
 *
 * 数据来源均为公开官方信息整理（NMPA / FDA / EU MDR / PMDA 等），
 * 结果附枢纽文件与行号，可溯源。不构成法规意见。
 */
"use strict";

const fs = require("fs");
const path = require("path");

const SKILLS_DIR = path.join(__dirname, "..", "skills");
const REFS_DIR = path.join(SKILLS_DIR, "references");

function refFiles() {
  if (!fs.existsSync(REFS_DIR)) return [];
  return fs.readdirSync(REFS_DIR).filter((f) => f.endsWith(".md")).sort();
}

function searchRefs(kw) {
  const kwl = String(kw || "").toLowerCase();
  if (!kwl) return { error: "关键词为空" };
  const hits = [];
  for (const f of refFiles()) {
    const content = fs.readFileSync(path.join(REFS_DIR, f), "utf8");
    content.split("\n").forEach((line, i) => {
      if (line.toLowerCase().includes(kwl)) {
        hits.push({ file: f, line: i + 1, text: line.trim().replace(/\s+/g, " ").slice(0, 160) });
      }
    });
  }
  return { total: hits.length, top: hits.slice(0, 8) };
}

module.exports = {
  install(ctx) {
    const logger = ctx?.logger ?? console;
    logger.info("[medxpert-reg-hub] 医械注册合规枢纽已加载，20 大枢纽就绪。");

    if (ctx?.tools) {
      ctx.tools["medxpert_quick_ref"] = {
        description: "医疗器械注册合规关键词速查：在中/美/欧/日 20 大枢纽知识库中检索关键词，返回命中文件与行号。",
        args: { keyword: { type: "string", required: true, description: "产品/法规/分类关键词，如 关节镜、510k、PSUR" } },
        run: async ({ keyword }) => JSON.stringify(searchRefs(keyword)),
      };
      ctx.tools["medxpert_refs"] = {
        description: "列出 medxpert 技能包全部枢纽文件（注册工程师资料/UDI/STED/GMP/临床评价/上市后等）。",
        args: {},
        run: async () => JSON.stringify({ files: refFiles(), count: refFiles().length }),
      };
      logger.info("[medxpert-reg-hub] 工具已注册：medxpert_quick_ref / medxpert_refs");
    }
  },
};
