#!/usr/bin/env node
/**
 * medxpert — 医疗器械全球注册合规速查 CLI
 * 零依赖（Node 内置模块），随 npm 包分发。
 *
 * 命令：
 *   medxpert info            包信息与技能导航
 *   medxpert refs            列出 references 全部枢纽文件
 *   medxpert quick <关键词>   在枢纽库中检索关键词（产品/法规/分类），返回命中文件与行
 *   medxpert check-links     扫描 SKILL.md/references 中的官方链接并报告可达性
 *
 * 数据源：包内 skills/references（20 大枢纽，官方源整理）。
 */
"use strict";

const fs = require("fs");
const path = require("path");
const http = require("http");
const https = require("https");

const PKG_ROOT = path.join(__dirname, "..");
const SKILLS_DIR = path.join(PKG_ROOT, "skills");
const REFS_DIR = path.join(SKILLS_DIR, "references");

function refFiles() {
  if (!fs.existsSync(REFS_DIR)) return [];
  return fs
    .readdirSync(REFS_DIR)
    .filter((f) => f.endsWith(".md"))
    .sort();
}

function pkg() {
  try {
    return JSON.parse(fs.readFileSync(path.join(PKG_ROOT, "package.json"), "utf8"));
  } catch {
    return {};
  }
}

function cmdInfo() {
  const p = pkg();
  const lines = [
    `medxpert-reg-hub v${p.version || "?"}`,
    `描述: ${p.description || ""}`,
    `技能: ${SKILLS_DIR}`,
    `枢纽文件数: ${refFiles().length}`,
    "",
    "用法:",
    "  medxpert refs              列出全部枢纽",
    "  medxpert quick <关键词>     枢纽库关键词速查",
    "  medxpert check-links       官方链接核验",
  ];
  console.log(lines.join("\n"));
}

function cmdRefs() {
  const files = refFiles();
  if (!files.length) {
    console.log("未找到 references 目录（包结构不完整）。");
    process.exit(1);
  }
  console.log(`共 ${files.length} 个枢纽文件:`);
  files.forEach((f, i) => console.log(`${String(i + 1).padStart(2)}. ${f}`));
}

function cmdQuick(keyword) {
  if (!keyword) {
    console.error("用法: medxpert quick <关键词>  （如: medxpert quick 关节镜）");
    process.exit(2);
  }
  const files = refFiles();
  const kw = keyword.toLowerCase();
  let hits = 0;
  for (const f of files) {
    const p = path.join(REFS_DIR, f);
    const content = fs.readFileSync(p, "utf8");
    const lines = content.split("\n");
    let match = [];
    lines.forEach((line, i) => {
      if (line.toLowerCase().includes(kw)) match.push(i + 1);
    });
    if (match.length) {
      hits += match.length;
      console.log(`\n📄 ${f}  (命中 ${match.length} 行)`);
      match.slice(0, 5).forEach((ln) => {
        const text = lines[ln - 1].trim().replace(/\s+/g, " ").slice(0, 140);
        console.log(`   L${ln}: ${text}`);
      });
      if (match.length > 5) console.log(`   … 其余 ${match.length - 5} 行`);
    }
  }
  console.log(`\n共命中 ${hits} 行（${files.length} 个枢纽文件）。`);
}

function checkUrl(url, timeoutMs) {
  return new Promise((resolve) => {
    const mod = url.startsWith("https") ? https : http;
    const req = mod.get(
      url,
      { timeout: timeoutMs, headers: { "User-Agent": "medxpert-reg-hub/2.0.1" } },
      (res) => {
        resolve({ url, code: res.statusCode });
        res.resume();
      }
    );
    req.on("timeout", () => {
      req.destroy();
      resolve({ url, code: 0, error: "timeout" });
    });
    req.on("error", (e) => resolve({ url, code: 0, error: e.message }));
  });
}

async function cmdCheckLinks() {
  const urlRe = /https?:\/\/[^\s)\]]+/g;
  const links = new Set();
  const targets = [path.join(SKILLS_DIR, "SKILL.md"), ...refFiles().map((f) => path.join(REFS_DIR, f))];
  for (const p of targets) {
    if (!fs.existsSync(p)) continue;
    const content = fs.readFileSync(p, "utf8");
    for (const m of content.match(urlRe) || []) {
      const clean = m.replace(/[),.;]+$/, "");
      if (/^https?:\/\//.test(clean)) links.add(clean);
    }
  }
  console.log(`扫描到 ${links.size} 个官方链接，抽样核验前 25 个…`);
  const sample = Array.from(links).slice(0, 25);
  let ok = 0;
  for (const url of sample) {
    const r = await checkUrl(url, 8000);
    const state = r.code >= 200 && r.code < 400 ? "OK" : `FAIL(${r.code || r.error})`;
    if (state === "OK") ok++;
    console.log(`  [${state}] ${url.slice(0, 90)}`);
  }
  console.log(`\n抽样 ${sample.length} 个，可达 ${ok} 个。完整核验见技能 references 导航。`);
}

async function main() {
  const cmd = process.argv[2] || "info";
  switch (cmd) {
    case "info": cmdInfo(); break;
    case "refs": cmdRefs(); break;
    case "quick": cmdQuick(process.argv.slice(3).join(" ")); break;
    case "check-links": await cmdCheckLinks(); break;
    default:
      console.error(`未知命令: ${cmd}`);
      cmdInfo();
      process.exit(2);
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
