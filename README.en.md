# MedXpert Medical Device Regulatory Compliance Skill Hub

> **⭐ Star this repo** — help more regulatory-affairs engineers find it: [GitHub](https://github.com/stevenzhao07/medxpert-reg-hub) · [中文版 README](./README.md) · **English** | 求星 + 语言切换

**Medical Device Global Regulatory Compliance Skill Hub** (Agent Skills standard) — a structured regulatory-intelligence hub organizing official sources from NMPA / FDA / EU MDR / PMDA / ASEAN / LATAM by *market x registration phase x product category*, covering the full lifecycle: product planning -> classification & pathway -> technical files -> QMS -> submission -> review & clearance -> post-market.

## Why this hub (48-case dual-track evidence)
We benchmarked a full 48-case run (2026-10-27) across all 22 catalog categories + AI medical software. **With this skill: 5.00 on all five dimensions (48/48).** Without it: 3.83 correctness / 2.19 traceability / 1.94 coverage / 1.25 boundary & timeliness / 1.94 pitfall identification. Same questions, same sources — the difference is the structured hub + verified links + anti-pattern knowledge. Internal dual-track benchmark, not third-party certification.

## Highlights
- **28 hubs / 33 references** of verified official links (119 links browser-verified, dead-link rate ~ 0).
- **Evaluation**: 48-case full dual-track run (2026-10-27) across all 22 catalog categories + AI medical software. Skill side: 5.00 on all five dimensions (48/48); no-skill baseline: 3.83 correctness / 2.19 traceability / 1.94 coverage / 1.25 boundary & timeliness / 1.94 pitfall identification. Internal dual-track benchmark, not third-party certification.
- **Multi-ecosystem native**: Agent Skills SKILL.md format loads in Claude Code / Codex / Cursor / DSH / Qwen / Kimi Claw / Zhipu Auto Claw; plus zero-dependency CLI and read-only MCP server.

## LGD ecosystem interlink
Built on [LGD (Lifecycle Governance Doctrine / 全程治理论)](https://github.com/zhaoxinghua09-cell/lgd-theory) — a governance theory for autonomous systems (entity registration spine · evidence gating · silent-failure detection · human authorization gate). This hub is a **reference implementation** of LGD in the regulated medical-device domain; the theory repo lists it as a landing example.

![LGD-Powered](https://raw.githubusercontent.com/zhaoxinghua09-cell/lgd-theory/main/assets/badges/powered/lgd-powered-en.svg)

Theory text: CC BY 4.0 · DOI 10.5281/zenodo.22456647 · Rights & attribution: see [llms.txt](./llms.txt).

## Install
```sh
npm install -g medxpert-reg-hub   # CLI + skill bundle
medxpert info                     # navigation
medxpert quick 关节镜              # keyword lookup
```
DeepSeek Harness plugin: `dsh plugin --profile web add medxpert-reg-hub`
MCP: configure mcp/server.json (5 read-only tools: udi_lookup / fda_510k_lookup / pma_lookup / class_lookup / hub_search)
Claude / Codex / Cursor: put the `skills/` folder into `.claude/skills/` (or `.cursor/skills/`).

## Structure
```
SKILL.md            bilingual skill manifest (triggers / workflow / SOPs / anti-patterns / boundaries)
references/         33 hubs (each with English title + summary frontmatter)
assets/             overview.svg + classification quick tool + LGD badges
scripts/            link check / compliance grading / sensitive scan / frontmatter validate
docs/               evaluation report + 48-case raw data
```

## Distribution
- GitHub: github.com/stevenzhao07/medxpert-reg-hub (topic dsh-plugin, Release v2.0.1 + tgz)
- awesome-dsh-plugin entry prepared (category: skill, tarball -> GitHub Release)
- MCP Registry / Glama / mcp.so / Smithery / SkillHub / Doubao skill center materials ready
- Web public layer: https://medxpert.cn/knowledge/

## License
MIT (c) 注册老炮 @ MedXpert. Compiled from public official information; not regulatory advice; verify against latest official releases before filing.
