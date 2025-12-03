# Obsidian Assistant

<p align="center">
  An intelligent multi-agent system for your Obsidian vault, powered by Google's Agent Development Kit.
  <br>
  <a href="https://github.com/pau-fortiana/obsidian-assistant-adk/issues">Report Bug</a>
  ·
  <a href="https://github.com/pau-fortiana/obsidian-assistant-adk/issues">Request Feature</a>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/release/python-3120/"><img src="https://img.shields.io/badge/Python-3.12+-blue.svg" alt="Python 3.12+"></a>
  <a href="https://github.com/pau-fortiana/obsidian-assistant-adk/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License"></a>
  <a href="https://github.com/pau-fortiana/obsidian-assistant-adk/stargazers"><img src="https://img.shields.io/github/stars/pau-fortiana/obsidian-assistant-adk.svg" alt="Stargazers"></a>
</p>

---

## About The Project

Obsidian Assistant is an intelligent multi-agent system designed to streamline your knowledge management within Obsidian. Built with Google's Agent Development Kit (ADK), this hierarchical multi-agent architecture transforms your vault from a static collection of notes into a dynamic knowledge base.

It goes beyond simple editing by acting as a complex task planner and software project assistant. It can define project steps, generate context files for AI agents, and even create new agent modes for your IDE.

Whether you're a student, a writer, or a lifelong learner, the Obsidian Assistant is here to help you connect ideas, uncover insights, and unlock the full potential of your second brain.

## Key Features

- **Seamless Note Management**: Create, edit, and organize your Markdown notes with simple commands.
- **Content Enhancement**: Automatically improve your notes with summaries, structural suggestions, and linting.
- **Obsidian Expertise**: Get guidance on Obsidian's features and workflows without leaving your vault.
- **Modular and Extensible**: Built with a modular, multi-agent architecture that is easy to maintain and extend.
- **Project Planning**: Design implementation plans and break down complex tasks into structured lists.
- **Developer-Friendly**: Create Markdown-based context files for agents and VSCode Agent Modes.

## Getting Started

Follow these simple steps to get the Obsidian Assistant up and running.

### Prerequisites

- Python 3.12+
- `uv` (Python package manager)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/pau-fortiana/obsidian-assistant-adk.git
    cd obsidian-assistant-adk
    ```

2. **Install `uv`:**

    ```sh
    pip install uv
    ```

3. **Setup Environment & Dependencies:**

    ```sh
    # Create a virtual environment
    uv venv
    
    # Activate the virtual environment
    source .venv/bin/activate

    # Sync dependencies
    uv sync
    ```

4. **Configuration:**

    Create a `.env` file in the project root to configure your assistant:

    ```env
    GOOGLE_API_KEY="your-gemini-api-key"
    OBSIDIAN_VAULT_PATH="/path/to/your/actual/obsidian/vault"
    ```

    *Note: If `OBSIDIAN_VAULT_PATH` is not set, the assistant will default to creating a new vault in `outputs/obsidian_vault`.*

## Usage

You can interact with the Obsidian Assistant in two ways:

- **Web Interface**: For a user-friendly, browser-based experience.
- **Command-Line**: For quick interactions directly from your terminal.

### Web Interface

Launch the web interface from the project root:

```bash
adk web
```

This will start a local server, and you can interact with the agent through your browser.

### Command-Line Interface

Run the agent from your terminal:

```bash
adk run obsidian_assistant
```

## License

Distributed under the Apache 2.0 License. See `LICENSE` for more information.

### Foundation Attribution

The core strategy and implementation logic for this ADK agent are directly derived from the following work, which is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) License:

- **Original Source:** Obsidian Assistant ([Kaggle](https://www.kaggle.com/) Submission Writeup for [`Agents Intensive - Capstone Project`](https://www.kaggle.com/competitions/agents-intensive-capstone-project/overview)) Community Hackaton.
- **Author(s):** Pau Fortiana Chico (paufortiana)
- **Link:** [Obsidian Assistant Writeup](https://www.kaggle.com/competitions/agents-intensive-capstone-project/writeups/obsidian-assistant)
- **Source Code (Apache License 2.0):** [Obsidian Assistant Notebook](https://www.kaggle.com/code/paufortiana/obsidian-assistant). A local copy of this source is included in this repository at [`notebooks/obsidian_agent.ipynb`](notebooks/obsidian_agent.ipynb).

Per the CC BY 4.0 terms, this adaptation provides clear and prominent attribution to the original source.

## Acknowledgments

- Powered by [Google's Agent Development Kit](https://google.github.io/adk-docs/).
