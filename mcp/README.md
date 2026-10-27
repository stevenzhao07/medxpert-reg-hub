# medxpert-reg-hub · MCP Server

`mcp-name: io.github.stevenzhao07/medxpert-reg-hub`

Read-only medical device regulatory MCP server. Tools (all read-only):

- `udi_lookup` — NMPA UDI queries (main DI / product name / registration no.)
- `fda_510k_lookup` — FDA 510(k) queries (K-number / company / product)
- `pma_lookup` — FDA PMA queries (PMA number / company / product)
- `class_lookup` — FDA product classification queries (product code / name)
- `hub_search` — keyword search across the 20-hub regulatory knowledge base (CN/US/EU/JP)

## Install & run

```bash
pip install medxpert-reg-hub
medxpert-mcp        # stdio MCP server
```

## Data (MEDXPERT_DB / MEDXPERT_REFS)

The PyPI wheel is metadata-light by design (the full dataset is ~600M+ rows across
SQLite). Point the server at your data:

```bash
export MEDXPERT_DB=/path/to/medxpert_device.sqlite
export MEDXPERT_REFS=/path/to/skills/references
medxpert-mcp
```

The reference data bundle is published in the GitHub repo
[stevenzhao07/medxpert-reg-hub](https://github.com/stevenzhao07/medxpert-reg-hub)
(docs/ and skills/references/), so you can clone it and set the env vars, or use
your own RA knowledge base.

License: MIT © 2026 MedXpert
