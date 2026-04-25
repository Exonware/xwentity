# xwentity

**Unified entity layer.** Ties schema (xwschema), actions (xwaction), and data (xwdata) together with metadata, caching, state, and XWNode. Used by xwmodels, xwbase, and the rest of the eXonware stack. Details live in `docs/`.

**Company:** eXonware.com · **Author:** eXonware Backend Team · **Email:** connect@exonware.com  

[![Status](https://img.shields.io/badge/status-beta-blue.svg)](https://exonware.com)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

---

## 📦 Install

```bash
pip install exonware-xwentity
pip install exonware-xwentity[lazy]
# Full stack used by xwentity flows
pip install exonware-xwentity[full]
```

`[full]` pulls the full variants of: `xwsystem`, `xwaction`, `xwdata`, `xwquery`, `xwschema`, and `xwnode`.

---

## 🚀 Quick start

```python
from exonware.xwentity import XWEntity
from exonware.xwschema import XWSchema

schema = XWSchema({"type": "object", "properties": {"name": {"type": "string"}, "age": {"type": "integer"}}})
entity = XWEntity(schema=schema, data={"name": "Alice", "age": 30})
print(entity.data["name"])
```

See [docs/](docs/) for metadata, state, and REF_* files.

---

## ✨ What you get

| Area | What's in it |
|------|----------------|
| **Entity** | One class for schema, actions, data, metadata, caching. |
| **Integration** | xwschema, xwaction, xwdata, XWNode. |
| **Lifecycle** | State and property discovery. |

## 🧱 Core model (explicit roles)

- **XWEntity** (`entity.py`) composes `XWSchema` + `XWAction` + `XWData`: validation contract, entity-scoped behavior, and multi-format data payloads.
- **XWCollection** (`collection.py`) is a logical, storage-agnostic collection of entities of the same type, with collection-level actions (search/bulk operations).
- **XWGroup** (`group.py`) manages multiple collections and supports nested parent/child groups, forming a tree structure for organization.
- **Shared foundation:** `XWCollection` and `XWGroup` directly extend `XWObject` (`xwsystem`), and `XWEntity` extends `AEntity` which extends `XWObject`, so all core entity types inherit the same lightweight identity/object base.

---

## 🌐 Ecosystem functional contributions

`xwentity` is the domain model backbone; other XW libs provide validation, behavior, data, and persistence layers around it.
You can use `xwentity` standalone as a domain modeling layer with only the components you need.
The broader XW stack is optional and is most relevant for enterprise and mission-critical systems that need fully integrated, self-hosted model infrastructure.

| Supporting XW lib | What it provides to xwentity | Functional requirement it satisfies |
|------|----------------|----------------|
| **XWSchema** | Schema definitions and validation contracts attached to entities. | Strong model integrity and versionable validation rules. |
| **XWAction** | Entity-scoped actions and workflow behavior. | Behavioral domain methods with consistent execution hooks. |
| **XWData** | Multi-format data payload support and transformation paths. | Portable model serialization/input across formats. |
| **XWNode** | Node/graph structural representation and traversal capabilities. | Rich relationships and graph-aware entity operations. |
| **XWSystem** | Base object model and shared runtime primitives. | Uniform identity/runtime behavior across entities, collections, and groups. |
| **XWStorage** | Persistence providers used by higher-level entity collections/groups. | Durable entity lifecycle management across storage backends. |

This combination is the differentiator: `xwentity` is not just a dataclass layer, it is a contract-validated domain core connected to action, data, and storage infrastructure.

---

## 📖 Docs and tests

- **Start:** [docs/INDEX.md](docs/INDEX.md) or [docs/](docs/).
- **Tests:** From repo root, follow the layout in this package (pytest or project runner).

---

## 📜 License and links

Apache-2.0 - see [LICENSE](LICENSE). **Homepage:** https://exonware.com · **Repository:** https://github.com/exonware/xwentity  


## ⏱️ Async Support

<!-- async-support:start -->
- xwentity includes asynchronous execution paths in production code.
- Source validation: 4 async def definitions and 1 await usages under src/.
- Use async APIs for I/O-heavy or concurrent workloads to improve throughput and responsiveness.
<!-- async-support:end -->
Version: 0.6.0.12 | Updated: 25-Apr-2026

*Built with ❤️ by eXonware.com - Revolutionizing Python Development Since 2025*
