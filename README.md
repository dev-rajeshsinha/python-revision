# 🐍 python-revision

> A long-term Python revision hub — collecting code, notes, exercises, and study materials from tutorials, books, workshops, and more.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

---

## 📌 About

This repository is a personal, evolving study space for revising and deepening Python knowledge. It is **not** tied to a single course or tutorial — instead, it grows over time as new topics are explored, practised, and documented.

Whether you are skimming for a quick reference or following along systematically, you will find structured notes, runnable scripts, and hands-on exercises here.

---

## 🎯 Goals

- Maintain a single organised place for all Python revision material.
- Build a habit of writing clean, well-documented practice code.
- Cover Python concepts from fundamentals through to advanced topics.
- Collect useful snippets, patterns, and examples from varied sources.

---

## 🗂️ Repository Structure

```
python-revision/
├── src/              # Runnable Python scripts organised by topic
│   ├── basics/       #   Variables, data types, operators, I/O
│   ├── control_flow/ #   Conditionals, loops
│   ├── functions/    #   Functions, lambdas, decorators
│   ├── oop/          #   Classes, inheritance, dunder methods
│   ├── modules/      #   Imports, packages, standard library
│   ├── file_io/      #   File handling, context managers
│   ├── exceptions/   #   Error handling, custom exceptions
│   └── advanced/     #   Generators, comprehensions, async, etc.
│
├── notes/            # Markdown notes and concept summaries
│   └── <topic>.md
│
├── exercises/        # Practice problems and solutions
│   ├── problems/     #   Problem statements
│   └── solutions/    #   Worked solutions
│
├── materials/        # PDFs, cheat-sheets, and external references
│
├── .gitignore
├── LICENSE
└── README.md
```

> **Note:** Not all folders exist yet — they are added as new topics are studied.

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8+** installed — download from [python.org](https://www.python.org/downloads/).

### Clone the repository

```bash
git clone https://github.com/dev-rajeshsinha/python-revision.git
cd python-revision
```

### Run a script

```bash
python src/basics/hello_world.py
```

### (Optional) Set up a virtual environment

```bash
python -m venv .venv

# Activate — macOS / Linux
source .venv/bin/activate

# Activate — Windows
.venv\Scripts\activate
```

No external dependencies are required for most scripts. If a topic-specific `requirements.txt` is present inside a folder, install it with:

```bash
pip install -r <folder>/requirements.txt
```

---

## 📐 Conventions

| Convention | Detail |
|---|---|
| **Script naming** | `snake_case.py`, descriptive and topic-specific |
| **Folder naming** | `snake_case/`, one folder per major topic |
| **Notes** | Markdown (`.md`) stored in `notes/`, named after the topic |
| **Exercises** | Problem in `exercises/problems/`, solution in `exercises/solutions/` |
| **Comments** | Inline comments explain *why*, not just *what* |
| **Versioning** | No date-based names — rely on Git history for chronology |

---

## ✅ Progress Tracker

Use this table to track topics as they are studied and revised.

| Topic | Notes | Scripts | Exercises | Status |
|---|---|---|---|---|
| Variables & Data Types | ☐ | ☐ | ☐ | 🔲 Not started |
| Control Flow | ☐ | ☐ | ☐ | 🔲 Not started |
| Functions | ☐ | ☐ | ☐ | 🔲 Not started |
| Object-Oriented Programming | ☐ | ☐ | ☐ | 🔲 Not started |
| Modules & Packages | ☐ | ☐ | ☐ | 🔲 Not started |
| File I/O | ☐ | ☐ | ☐ | 🔲 Not started |
| Exception Handling | ☐ | ☐ | ☐ | 🔲 Not started |
| Comprehensions | ☐ | ☐ | ☐ | 🔲 Not started |
| Generators & Iterators | ☐ | ☐ | ☐ | 🔲 Not started |
| Decorators | ☐ | ☐ | ☐ | 🔲 Not started |
| Standard Library | ☐ | ☐ | ☐ | 🔲 Not started |
| Testing (unittest / pytest) | ☐ | ☐ | ☐ | 🔲 Not started |

> **Legend:** ✅ Done · 🔄 In progress · 🔲 Not started

---

## 📚 Resources

| Resource | Type | Link |
|---|---|---|
| Official Python Docs | Documentation | [docs.python.org](https://docs.python.org/3/) |
| Python Tutorial (official) | Tutorial | [docs.python.org/3/tutorial](https://docs.python.org/3/tutorial/) |
| Real Python | Articles & Tutorials | [realpython.com](https://realpython.com/) |
| Automate the Boring Stuff | Book (free online) | [automatetheboringstuff.com](https://automatetheboringstuff.com/) |
| Python Cheatsheet | Quick Reference | [pythoncheatsheet.org](https://www.pythoncheatsheet.org/) |
| Exercism — Python Track | Practice Exercises | [exercism.org/tracks/python](https://exercism.org/tracks/python) |

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE) — feel free to use, adapt, and share any content here.

---

<p align="center">Made with ❤️ for continuous learning</p>
