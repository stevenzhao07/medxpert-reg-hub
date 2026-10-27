# medxpert-reg-hub · 医械全球注册合规技能聚合包

> **Medical Device Global Regulatory Compliance Skill Hub** — 医疗器械全球注册合规的**结构化资料枢纽**（Agent Skills 标准格式），把 NMPA / FDA / EU MDR / PMDA 及各市场官网的法规、标准、申报系统、模板，按「市场 × 注册阶段 × 产品类别」整理成可点击直达的官方源。

---

## What is this? / 这是什么

**EN** — A structured regulatory-intelligence hub for medical-device regulatory affairs (RA) engineers. 28 references organize official sources from NMPA / FDA / EU MDR / PMDA / ASEAN / LATAM by *market × registration phase × product category*, covering the full lifecycle: product planning → classification & pathway → technical files → QMS → submission → review & clearance → post-market. Every conclusion links to official sources; boundaries are honestly flagged as "to be verified / apply for classification determination" rather than guessed. Includes a zero-dependency CLI and a read-only DSH plugin / MCP server.

**CN** — 医疗器械注册工程师的**结构化资料枢纽**。把分散在 NMPA / FDA / EU MDR / PMDA 及各市场官网的法规、标准、申报系统、模板，按「市场 × 注册阶段 × 产品类别」整理成可点击直达的官方源。覆盖从**产品立项 → 分类与路径 → 技术文件 → 质量体系 → 注册申报 → 审评获批 → 上市后**的全流程。每个结论附官方直达链接，边界情形明确标注"待核验 / 走分类界定"，不误导。

---

## 全生命周期 7 阶段 · 28 枢纽 / Lifecycle: 7 phases, 28 hubs

```text
需求立项 → 分类路径 → 技术文件 → 质量体系 → 注册申报 → 审评获批 → 上市后
    │          │          │          │          │          │          │
  立项/需求    NMPA/     STED/CTD   GMP/ISO    eRPS/      审评时限    PMS/UDI/
   调研        FDA/MDR   撰写       13485      申报实操    核查获证    上市后监管
    └─────────────── 覆盖中/美/欧/日/东南亚/拉美 ─────────────────┘
```

| # | Hub (EN) / 枢纽（中文） | 用途 Purpose |
|---|---|---|
| 1 | 注册工程师资料枢纽 · RA Engineer Hub（主索引） | 中/美/欧/日及全球主要市场，按 7 阶段排列的官方资料直达 |
| 2 | 枢纽总览·全生命周期 7 阶段纲领 · Lifecycle Overview | 7 阶段总纲：需求立项→分类路径→技术文件→质量体系→注册申报→审评获批→上市后 |
| 3 | UDI 全球标识枢纽 · Global UDI | 中美欧 UDI 规则、发码机构、数据库 |
| 4 | 技术文件 STED 撰写枢纽 · STED/CTD Technical Files | STED 结构、CTD 思路、各模块撰写要点 |
| 5 | 注册周期·费用·有效期对比枢纽 · Cycle/Cost/Validity | 各市场周期/费用/证书有效期的横向比对 |
| 6 | 原材料供应商合规枢纽 · Supplier Compliance | 供应商资质、材质证明、13485/ROHS/REACH |
| 7 | GMP 质量体系与验证枢纽 · GMP/QMS & Validation | GMP/ISO 13485、工艺验证、再处理验证 |
| 8 | 生物相容性测试规划枢纽 · Biocompatibility | ISO 10993 系列、终点选择、试验规划 |
| 9 | 上市后监管枢纽 · Post-Market Surveillance | 不良事件、召回、PMS、FSCA |
| 10 | 标签与 IFU 枢纽 · Labeling & IFU | 标签要素、IFU 编写、多语言要求 |
| 11 | 需求调研与立项枢纽 · Requirement & Initiation | 需求挖掘/竞品分析(官方库)/PRD/设计输入/立项评审 |
| 12 | 风险管理枢纽 · Risk Management | ISO 14971 六步流程/风险文件入卷位置 |
| 13 | 设计开发控制枢纽 · Design Control | ISO 13485 7.3 / 21 CFR 820.30 九步：输入输出/评审/V&V/转移/变更 |
| 14 | 软件人因枢纽 · Software & Human Factors | IEC 62304 / IEC 62366 / SaMD 分类 / 网络安全 |
| 15 | 灭菌包装验证枢纽 · Sterilization & Packaging | 灭菌选型/过程确认 IQOQPQ/无菌屏障 ISO 11607 |
| 16 | 注册检验与申报实操枢纽 · Testing & Submission | 型检(委托/自检126号)/eRPS/eSTAR/EUDAMED/PMDA/发补应对 |
| 17 | 审评核查获证枢纽 · Review & Clearance | 审评时限/体系核查/获证后合规 |
| 18 | 临床评价枢纽 · Clinical Evaluation | 三条路径/免临床目录/CER 撰写要点 |
| 19 | 变更延续管理枢纽 · Change & Renewal | 变更/延续注册/新510(k)/重大变更 |
| 20 | 售后服务枢纽 · After-Sales Service | 投诉与不良事件上报边界/维修备件/培训 |
| 21 | 市场准入与销售枢纽 · Market Access & Sales | 经营资质/出口销售证明(2026-05新规)/注册列名 |
| 22 | 骨科手术器械 全球注册路径实证 · Orthopedic Devices Evidence | 13 市场真实注册证验证的分类结论 |
| 23 | 分类判定速查 · Classification Quick Reference | 常见品类分类速查与判定分水岭 |
| 24 | 召回实证速查 · Recalls Quick Reference | 中/美/欧召回案例与上报要点速查 |
| 25 | 国际业务经营枢纽 · International Business | 跨境销售/代理商/授权代表实务 |
| 26 | 注册申报资料汇编 · Submission Package | 各市场申报资料清单汇编 |
| 27 | 合规度评分 · Compliance Score | 8 大维度 × 0-5 分自评工具 |
| 28 | 市场实务（UDI 实施 / MDR PMS / MAH 委托生产 / FDA 供应链穿透）· Market Practices | 中美欧实务专题：EUDAMED 结构、GUDID、Art.83-92 PMS、MAH 委托、供应链核查 |

---

## 实测结果 / Evaluation（2026-10-27 双轨 48 实例全量实跑）

> **口径**：按《医疗器械分类目录》22 个大类（01–22）每类实跑 2 例 + 医疗 AI 类 5 例（医用软件类 6 例），共 **48 实例**；每例同时以「**技能侧**（本包加载）」与「**无技能侧**（通用 AI + 直接搜索）」作答，五维评分（正确性 / 可溯源性 / 覆盖度 / 边界与时效 / 坑点识别）。

| 维度 Dimension | 技能侧 With skill | 无技能侧 Without skill |
|---|---|---|
| 正确性 Correctness | **5.00** | 3.83 |
| 可溯源性 Traceability | **5.00** | 2.19 |
| 覆盖度 Coverage | **5.00** | 1.94 |
| 边界与时效 Boundary & Timeliness | **5.00** | 1.25 |
| 坑点识别 Pitfall Identification | **5.00** | 1.94 |

- **技能侧 48/48 五维全 5.0（100%）**；无技能侧最优维度仅 3.83，边界/时效维度 1.25。
- **增益判定**：高 7 例 / 中高 23 例 / 中 18 例——无技能侧普遍"答得出类别、答不出分水岭/申报面/中美差异/证据链"。
- **典型差异**：三类 vs 二类误判分水岭（生命支持宣称、软件辅助决策升类）、免临床目录内≠免资料、耗材直觉误判三类、无菌条件翻转类别、Ⅱ类(中国) vs Ⅰ类豁免(美国) 分类倒挂等。
- ⚠️ **诚实标注**：以上为**本包自建的内部双轨评测**（对比基线=通用 AI 直搜），非第三方机构认证；评测原始数据见仓库 `EVALUATION/`（48 例明细）。

---

## 安装 / Install

**npm（CLI + 技能包）**
```sh
npm install -g medxpert-reg-hub        # CLI + skill bundle
medxpert info                          # 查看导航 / show navigation
medxpert quick 关节镜                   # 关键词速查 / keyword lookup
medxpert check-links                   # 官方链接核验 / verify official links
```

**DeepSeek Harness 插件**
```sh
dsh plugin --profile web add medxpert-reg-hub
```

**MCP Server（UDI / 510k / PMA / 分类 / 枢纽检索，5 只读工具）**
```sh
npx medxpert-reg-hub-mcp   # 或按 mcp/server.json 配置
```

**Claude Code / Codex / Cursor / 千问 / Kimi Claw / 智谱 Auto Claw**
把 `skills/` 目录放入 `.claude/skills/`（或 `.cursor/skills/`、对应生态 skills 目录）即可——SKILL.md 为标准 Agent Skills 格式，全生态原生加载。

---

## 目录结构 / Structure

```
skills/
  SKILL.md          技能主文件（中英双语：触发/工作流/SOP/反模式/边界）
  references/       28 枢纽（含英文摘要导航）
  assets/           全景图 overview.svg + 分类速查工具.html
bin/medxpert.js     CLI（零依赖）
src/index.js        DSH 插件入口（只读工具）
mcp/server.py       MCP server（5 只读工具）
```

## 官方链接核验 / Link Verification

- 119 条官方链接经浏览器级复核（2026-08-14；2026-08-18 增补实务文件后已复核），死链率趋近于零（EUDAMED 旧入口偶发维护、器审中心为 JS 渲染站，均非死链）。
- FDA/ISO 官网对脚本探测返 404/403 属反爬正常现象，浏览器可正常打开；判定失效以浏览器级核验为准。

## 收录状态 / Distribution

- GitHub 仓库：`github.com/stevenzhao07/medxpert-reg-hub`（topic: `dsh-plugin`，Release v2.0.1 + 预构建 tgz）
- awesome-dsh-plugin 收录条目已备（category: skill，tarball 指向 GitHub Release）
- MCP Registry / Glama / mcp.so / Smithery / SkillHub / 豆包技能中心 素材已就绪
- 官网公开层：`https://medxpert.cn/knowledge/`（20+ 枢纽在线可读、AI 可访问）

## 许可 / License

MIT License © 注册老炮 @ MedXpert。内容为公开官方信息整理，**不构成法规意见**；实际申报以监管机构最新发布与专业 RA 判断为准。
