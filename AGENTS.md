# Agents - Project Context

This document provides instructional context for the Gemini CLI and any other agents working within this codebase, helping them understand the project's structure, purpose, and conventions.

## Project Overview

This is a Python project for an "Obsidian Assistant," an agent designed to help manage a Markdown-based Obsidian vault. It is built using Google's Agent Development Kit (ADK).

The assistant's primary capabilities include:

- Creating, reading, and improving notes.
- Providing guidance on Obsidian features and workflows.
- Assisting with project planning and generating Markdown-based documentation.

The core logic is structured around the `google-adk` library, with agent definitions located in the `obsidian-assistant/` directory.

## Building and Running

### Dependencies

The project's dependencies are managed using `pip` or `uv` and are defined in `pyproject.toml`.

- **Primary Dependency:** `google-adk`

### Setup and Execution

1. **Environment Setup:**
    - It is recommended to use a virtual environment.
    - The `README.md` suggests installing dependencies from a `requirements.txt`, but dependencies are listed in `pyproject.toml`. To install, you can run:

      ```bash
      # Using pip
      pip install .

      # Using uv
      uv pip install .
      ```

2. **API Key:**
    - The application requires a Gemini API key. It should be set as an environment variable:

      ```bash
      export GOOGLE_API_KEY="your-key"
      ```

3. **Running the Agent:**
    - The `README.md` indicates that the primary interaction method is through a CLI workflow.
    - A minimal CLI entry point exists in `main.py`, which currently prints a hello message.
    - Another interaction method is through a notebook workflow, where users can run cells in a Jupyter notebook to interact with the agent (not provided yet in the repo, the foundation source code of this codebase is a kaggle notebook).

## Development Conventions

- **Packaging:** The project uses `pyproject.toml`, indicating a modern Python packaging approach.
- **Structure:** The main application logic is contained within the `obsidian-assistant/` directory. The `main.py` file serves as a potential future entry point for a CLI.
- **Agent Definition:** Agents are defined using the `Agent` class from the `google.adk` library, as seen in `obsidian-assistant/agent.py`.
