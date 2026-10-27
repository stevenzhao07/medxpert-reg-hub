# medxpert-reg-hub · MCP Server

医疗器械全球注册合规**数据查询 MCP Server**（只读）。

把 medxpert 知识库数据直接变成 Agent 可调用的工具——任何支持 MCP 的助手（Claude、Cursor、DeepSeek、豆包、智谱等）都能实时查：
NMPA UDI（629 万条）· FDA 510(k)（16.8 万条）· FDA PMA（5.7 万条）· FDA 产品分类（7,088 条）· 20 大枢纽知识库速查。

## 工具

| 工具 | 说明 |
|---|---|
| `udi_lookup` | NMPA UDI：主DI 精确 / 产品名 / 注册证号模糊 |
| `fda_510k_lookup` | FDA 510(k)：K 号 / 申请公司 / 产品名 |
| `pma_lookup` | FDA PMA：PMA 号 / 公司 / 产品 |
| `class_lookup` | FDA 产品分类（21 CFR）：产品代码（如 HRX）/ 产品名 |
| `hub_search` | 20 大枢纽知识库关键词检索（中/美/欧/日注册路径） |

## 安装

```sh
pip install mcp>=2.1.1
```

## 运行

```sh
# stdio 模式（默认）
python server.py

# 指定数据路径（可选环境变量）
set MEDXPERT_DB=D:\Workbuddy\02-知识库\MedXpert-RA-Data\db\medxpert_device.sqlite
set MEDXPERT_REFS=D:\Workbuddy\08-理论体系\发布\技能治理\medxpert-reg-hub-npm\skills\references
python server.py
```

## 接入示例

**Claude Code**（`.mcp.json`）：
```json
{
  "mcpServers": {
    "medxpert-reg-hub": {
      "command": "python",
      "args": ["D:/Workbuddy/08-理论体系/发布/技能治理/medxpert-mcp/server.py"],
      "env": {"MEDXPERT_DB": "D:/Workbuddy/02-知识库/MedXpert-RA-Data/db/medxpert_device.sqlite"}
    }
  }
}
```

**Cursor / DSH / 豆包工作**：同样配置 `command + args` 即可。

## 查询效果

- `udi_lookup(di="06977181060182")` → 他克莫司测定试剂盒（化学发光免疫分析法），附注册证/分类/发码日期
- `class_lookup(product_code="HRX")` → Arthroscope（关节镜，21 CFR 分类）
- `hub_search("关节镜")` → 跨 13 个枢纽命中 33 行分类与路径要点

## 边界

- 只读查询，不修改任何数据
- 数据为公开监管数据整理（NMPA/FDA 官方源），查询结果以官方最新发布为准
- 不构成法规意见/注册代理服务

## 许可

MIT License © 注册老炮 @ MedXpert
