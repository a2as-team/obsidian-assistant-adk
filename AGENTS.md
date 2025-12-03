# Agents - Project Context

This document provides instructional context for the Gemini CLI and any other agents working within this codebase, helping them understand the project's structure, purpose, and conventions.

## Project Overview

This is a Python project for an "Obsidian Assistant," an agent designed to help manage a Markdown-based Obsidian vault. It is built using Google's Agent Development Kit (ADK).

The assistant's primary capabilities include:

- Creating, reading, and improving notes.
- Providing guidance on Obsidian features and workflows.
- Assisting with project planning and generating Markdown-based documentation.

The core logic is structured around the `google-adk` library, with agent definitions located in the `obsidian_assistant/` directory.

## Architecture & Hierarchy

The system follows a hierarchical multi-agent pattern:

1. **Root Agent** (`obsidian_assistant/agent.py`): The orchestrator that delegates tasks.
2. **Specialized Agents** (`obsidian_assistant/agents/tool_agents/`):
    - **Content Agents**: Summarization, outlining, and key point extraction.
    - **Format Agents**: Linting, templating, and style enforcement.
    - **Write Agents**: Quick logging and content review.
    - **Browse Agents**: Web search and documentation lookup.
3. **Tools Layer** (`obsidian_assistant/tools/`):
    - **Parser Tools**: Markdown and CSV parsing.
    - **Template Tools**: Predefined content and structure templates.
    - **Utility Tools**: Miscellaneous helper functions and classes.

## Building and Running

### Dependencies

The project's dependencies are managed using `uv` and are defined in `pyproject.toml`.

- **Primary Dependency:** `google-adk`

### Setup and Execution

1. **Environment Setup:**
    - It is recommended to use a virtual environment.
    - To install the project and its dependencies, first install `uv`, then create a virtual environment and sync the dependencies.

      ```bash
      # Install uv
      pip install uv

      # Create a virtual environment
      uv venv

      # Activate the virtual environment
      source .venv/bin/activate

      # Sync dependencies
      uv sync
      ```

2. **API Key:**
    - The application requires a Gemini API key. It should be set as an environment variable:

      ```bash
      export GOOGLE_API_KEY="your-key"
      ```

3. **Running the Agent:**

The project is run using the `adk` command-line tool.

There are two primary ways to interact with the Obsidian Assistant:

**Web Workflow**
Use the `adk web` command to launch a web-based interface for the agent from project root.

```bash
adk web 
```

- **CLI Workflow**
Use the `adk run path/to/my/agent` command to interact with the agent from your terminal.

```bash
adk run obsidian_assistant
```

## Development Conventions

- **Packaging:** The project uses `pyproject.toml`, indicating a modern Python packaging approach.
- **Structure:** The main application logic is contained within the `obsidian_assistant/` directory.
- **Agent Definition:** The root agent is defined in `obsidian_assistant/agent.py`.
