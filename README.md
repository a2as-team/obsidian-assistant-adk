# Obsidian Assistant (ADK Agent)

## Overview

Obsidian Assistant is an agent built with Google’s Agent Development Kit (ADK) to help manage a Markdown-based Obsidian vault. It can create, read, and improve notes, and provide guidance on Obsidian features.

## Features

- Create, edit, and organize Markdown notes
- Improve note content (summaries, structure, linting suggestions)
- Guidance on Obsidian features and workflows
- Modular, multi-agent architecture for maintainability
- Design project implementation plans with structured task lists
- Create markdown context files for agents and readmes
- Create markdown based VSCode Agent Modes

## Prerequisites

- Python 3.12+
- pip (or uv)

## Setup

```bash
# Optional: create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
# or, if you use uv
uv pip install -r requirements.txt
```

## Configuration

Set your Gemini API key (Linux/macOS):

```bash
export GOOGLE_API_KEY="your-key"
```

## Usage

There are two primary ways to interact with the Obsidian Assistant:

- CLI workflow: if a CLI entry point is added later, it will be documented here.
- Notebook workflow: open your project’s notebook (if present) and run cells to interact with the agent.

## Roadmap

- CLI runner backed by YAML-based agent definitions
- Vault utilities (templating, link management, linting)
- Expanded tool integrations (web search, summarization)

## Licensing and Attribution

The code in this repository is licensed under the **Apache License 2.0** (see the LICENSE file).

---

### Foundation Attribution

The core strategy and implementation logic for this ADK agent are directly derived from the following work, which is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) License:

- **Original Source:** Obsidian Assistant ([Kaggle](https://www.kaggle.com/) Submission Writeup for [`Agents Intensive - Capstone Project`](https://www.kaggle.com/competitions/agents-intensive-capstone-project/overview)) Community Hackaton.
- **Author(s):** Pau Fortiana Chico (paufortiana)
- **Link:** [Obsidian Assistant Writeup](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/obsidian-assistant)
- **Source Code (Apache License 2.0):** [Obsidian Assistant Notebook](https://www.kaggle.com/code/paufortiana/obsidian-assistant)

Per the CC BY 4.0 terms, this adaptation provides clear and prominent attribution to the original source.
