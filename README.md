# medxpert-reg-hub

医疗器械全球注册合规 **技能聚合包**（Agent Skills 标准格式）。

**20 大枢纽 · 中/美/欧/日/东南亚/拉美 · 48 实例双轨实测**

- 覆盖：产品立项 → 分类路径 → 技术文件 → 质量体系 → 注册申报 → 审评获批 → 上市后全生命周期
- 官方源直达：每个结论附 NMPA / FDA / EU MDR / PMDA 官方链接，可溯源
- 48 实例实测：技能侧分类正确 **48/48（100%）**；无技能侧 1/48（2.1%）——五维均值全面领先
- 多生态原生兼容：Claude Code / OpenAI Codex / Cursor / DeepSeek Harness / 通义千问 / Kimi Claw / 智谱 Auto Claw

## 安装

```sh
npm install -g medxpert-reg-hub        # CLI + 技能包
medxpert info                          # 查看导航
medxpert quick 关节镜                   # 关键词速查
medxpert check-links                   # 官方链接核验
```

DeepSeek Harness 插件安装：

```sh
dsh plugin --profile web add medxpert-reg-hub
```

Claude / Codex / Cursor：把 `skills/` 目录放入 `.claude/skills/`（或 `.cursor/skills/`）即可。

## 目录

```
skills/
  SKILL.md          技能主文件（触发/工作流/SOP/反模式/边界）
  references/       20+ 枢纽（注册工程师资料、UDI、STED、GMP、生物相容、
                     上市后监管、临床评价、变更延续、市场准入、召回实证速查等）
  assets/           全景图 overview.svg + 分类速查工具.html
bin/medxpert.js     CLI（零依赖）
src/index.js        DSH 插件入口（只读工具）
```

## 收录

- DeepSeek Harness 插件市场：`dsh plugin --profile web add medxpert-reg-hub`
- awesome-dsh-plugin 收录条目已备妥，待 GitHub 仓库上架后提交 PR（category: skill）

## 许可

MIT License © 注册老炮 @ MedXpert。内容为公开官方信息整理，不构成法规意见；实际申报以监管机构最新发布为准。
