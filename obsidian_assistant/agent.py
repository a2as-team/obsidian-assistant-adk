"""
This module serves as the main entry point for the Obsidian Assistant ADK application.

It initializes the ADK App, sets up the root agent, and configures the overall
application behavior.

"""
from google.adk.apps.app import App
from google.adk.agents.llm_agent import LlmAgent
from .adk_models import model_pro
from .agents.sub_agents.context_file_specialist.agent import context_file_agent
from .agents.sub_agents.vscode_specialist.agent import vscode_specialist_agent
from .agents.sub_agents.existing_content_edit.agent import existing_content_editor
from .agents.sub_agents.new_content_craft.agent import new_content_crafter
from .agents.sub_agents.task_planning.agent import task_plan_agent
from .tools.file_tools import list_notes, read_note, delete_note, merge_notes
from .tools.write_tools import quick_log, review
from .tools.browse_tools import search_tool, docs_tool

# Define the root agent

root_agent = LlmAgent(
    name="ObsidianAgent",
    model=model_pro,
    instruction="""You are the Obsidian Agent, the root orchestrator for a markdown knowledge base.

    **Role & Responsibilities**:
    - Your main purpose is to analyze the user intent and route requests to the appropriate tools or agents.

    **Tools**:
    A. File Manipulation:
    - `list_notes`: list notes in the vault.
    - `read_note`: read existing notes.
    - `delete_note`: remove notes.
    - `merge_notes`: combine notes.
    B. Tool Agents (agents that understand user intent):
    - `ReviewAgent`: to review existing notes.
    - `DocumentationAgent`: for Obsidian documentation questions.
    - `SearchAgent`: for web research.
    - `QuickLogger`: to create, append or update notes.

    **Sub-Agents**:
    - `ContextFileAgent`: to create project context files.
    - `VSCodeSpecialist`: to create VS Code Copilot agent definitions.
    - `ExistingContentEditor`: to edit existing notes.
    - `NewContentCrafter`: to create new notes.
    - `TaskPlanner`: to create structured plans.

    **Guidelines and Workflow**:
    - Carefully analyze user intent to determine if they want to create new content, edit existing notes, or simply ask a question.
    - Use the *Routing Table* to determine the appropriate agent/tool for each task (consider *a* and *b* IF *create* or *edit*):
        a. To CREATE new documents, decide whether to use `QuickLogger` (simple tasks, you can provide the full content)
        or `NewContentCrafter` for complex tasks (slow iterative write).
        b. To EDIT documents decide, based on the complexity of the request, whether to append to document or replace content
        using `QuickLogger` (for small documents, you can provide the updated content) or, call `ExistingContentEditor` (slow iterative rewrite).
    - To MERGE/COMBINE documents (not just appending one note to another), use `merge_notes` and provide the merged document to `ExistingContentEditor`.
    - For simple questions or research, use `SearchAgent` and `DocumentationAgent` (call `QuickLogger` to create a file if needed).
    - Always verify file targets with `list_notes` and ask user for confirmation if files exists with similar names.
    - Ensure user confirmation before using destructive actions (e.g. delete, merge).

    **Routing Table**:

    | User Intent                                                | Agent/Tool                     |
    |------------------------------------------------------------|--------------------------------|
    | *Quick* logs, journals, lists (create, update or append)   | `QuickLogger`                  |
    | *Create* refined new documents, blogs, research            | `NewContentCrafter`            |
    | *Edit*, refine, or rewrite existing documents              | `ExistingContentEditor`        |
    | Create or update *Developer* Context (AGENTS.md, README)   | `ContextFileAgent`             |
    | Create *VS Code Copilot* Custom Agent definitions          | `VSCodeSpecialist`             |
    | *Plan* structured goals or project roadmaps                | `TaskPlanner`                  |
    | *Obsidian documentation* questions                         | `DocumentationAgent`           |
    | *Search* information, facts or examples and templates      | `SearchAgent`                  |
    """,
    
    tools=[
        list_notes, read_note, delete_note, merge_notes, # Function Tools
        review, quick_log, docs_tool, search_tool, # Tool Agents
    ],
    sub_agents=[task_plan_agent, context_file_agent, vscode_specialist_agent, # Specialized Agents
                existing_content_editor, new_content_crafter], # Workflow Agents
    output_key="root_response",
)

app = App(
    name="obsidian_assistant",
    root_agent=root_agent,
    # Optionally include App-level features:
    # plugins, context_cache_config, resumability_config
)