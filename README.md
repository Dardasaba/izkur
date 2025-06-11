# ❛❛❞ Izkur – Israeli Legal Citation Parser

**Izkur** (אִזְכּוּר, "citation" in Hebrew) is a Python library for parsing, analyzing, and generating structured representations of Israeli legal citations. It follows the 3rd edition of the official guide _"כללי האזכור האחיד בכתיבה המשפטית"_ and is built with compiler-inspired components for clarity, maintainability, and correctness.

---

## 🚀 Project Goals

- 🏛 Parse Israeli legal citations into structured, queryable data.
- ⚖️ Support multiple citation types: cases, statutes, books, articles, etc.
- 🧠 Enable CLI, JSON, and Python API usage.
- 🧩 Use compiler techniques: lexical analysis, parsing, semantic analysis.
- 🧰 Provide extensible Symbol Table and Error Handling infrastructure.

## 🧱 Architecture Overview

| Phase                | Component                | Description                                   |
|---------------------|--------------------------|-----------------------------------------------|
| Lexical Analysis     | `tokenizer/`              | Splits text into tokens.                      |
| Syntax Analysis      | `parser/`                 | Builds AST from token stream.                 |
| Semantic Analysis    | `symbols/`, `errors/`     | Validates structure, resolves entities.       |
| Code Generation      | `__str__`, `to_json`      | Converts back to citation or structured data. |

## 📁 Directory Layout

```shell
izkur/
├── tokenizer/          # Lexical analysis: token definitions & scanner
├── parser/             # Syntax analysis: grammar and AST generation
├── symbols/            # Symbol tables for cases, laws, etc.
├── errors/             # Centralized error reporting & recovery
├── models/             # Core domain models (e.g., Case, Legislation)
├── cli/                # Command-line interface (using Typer)
├── api/                # API
├── config/             # Configuration
├── tests/              # Unit and integration tests
└── init.py
```

## 📦 Installation

via `pip`:

```bash
pip install izkur
```

Or if you prefer using `uv`:

```bash
uv add izkur
```

(Or clone the repo and use uv or hatch if you're developing.)

## 🔧 Usage Examples

From Python

```python
from izkur import parse_citation

citation = 'בג"ץ 1234/22 פלוני נ׳ מדינת ישראל'
result = parse_citation(citation)
print(result.to_dict())
```

From CLI

```bash
izkur parse 'ע"פ 5678/21 מדינת ישראל נ׳ אלמוני'
```

## 🧪 Running Tests

```bash
pytest
```

Or, if using hatch:

```bash
hatch run test
```

## 🧠 Components in Detail

### 🗂️ Symbol Table

Keeps track of known courts, laws, abbreviations, collections.

Used during semantic analysis for validation and normalization.

### ⚠️ Error Handler

Centralizes error reporting by stage: lexical, syntactic, semantic.

Errors are recoverable and can be displayed with position info.

## 🧭 Roadmap

[x] Tokenizer and basic AST scaffolding

[x] Error handler

[ ] PEG-based parser

[ ] Support all citation types

[ ] Export to Bluebook / OpenCitations JSON formats

[ ] Web interface for testing and visualization

## 🤝 Contributing

Want to help? Awesome.

1. Fork and clone
1. Create a branch
1. Write tests and code
1. Submit PR

## 📃 License

MIT License © 2025 Dardasaba

## 📚 References

- Specification: [כללי האזכור האחיד בכתיבה המשפטית, מהדורה שלישית](https://law.tau.ac.il/sites/law.tau.ac.il/files/media_server/law_heb/izkur/izkur2021pdf.pdf)
- Python PEG Parser
- Compiler Design Books
