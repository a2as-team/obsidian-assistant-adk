"""
This module defines a multi-agent system for editing existing content within the
Obsidian Assistant.

It comprises several specialized agents:
- `LoadDocsAgent`: Loads existing notes and edit instructions.
- `DocumentRewriter`: Creates the initial draft based on existing content and instructions.
- `RefinementEditCritic`: Critiques the draft and provides actionable feedback.
- `RefinementEditWriter`: Applies the feedback to refine the draft.
- `RefineEditAgent`: Manages the iterative critique and refinement loop.
- `UpdaterAgent`: Saves the final, refined document back to the file system.
The `ExistingContentEditor` orchestrates these agents to provide a robust
and iterative content editing workflow.
"""
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.loop_agent import LoopAgent
from adk_models import model_pro, model_flash, model_flash_lite
from tools.file_tools import list_notes, read_note, update_note
from tools.browse_tools import search_tool, docs_tool
from tools.content_tools import outline, breakdown
from tools.format_tools import style, template, lint
from tools.write_tools import review

COMPLETION_PHRASE = "No major issues found."

def exit_loop(tool_context):
  """Call only when the critic responds with the completion phrase to stop the refinement loop."""
  print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
  tool_context.actions.escalate = True
  return {}

# The document loader just loads existing content and instructions for edits into state variables
load_docs_agent = LlmAgent(
    name="LoadDocsAgent",
    model=model_flash_lite,
    description="Load an existing note and interpret edit instructions.",
    instruction="""You load text from files and output it.
    **Tools**:
    - `read_note`: Read the content of an existing note.
    - `list_notes`: List available notes to find the target note if needed.
    **Guidelines**:
    - Use `list_notes` to verify the filename if there are typos.
    - You don't need to summarize or analyze the content here; just load it using `read_note`.
    **CRITICAL RULE: DO NOT STOP TO ASK QUESTIONS.**
    **Task**:
    1. Identify the file the user wants to edit.
    2. Call `read_note` to get the content.
    3. Output the content into `existing_document` with the following format:
    ```Instructions:
    {user's edit instructions here including the filename}
    Existing Document:
    {file content here}
    ```
    **Output**:
    - Return *only* the `existing_document` and `instructions`.""",
    tools=[read_note, list_notes], # Needs list_notes in case of typo in filename
    output_key="existing_document"
)

# The document rewriter receives the existing content and instructions to produce the first draft
document_rewriter = LlmAgent(
    name="DocumentRewriter",
    model=model_pro,
    description="Create the first markdown draft using research context.",
    instruction="""You are the Document Rewriter Specialist for the Obsidian Agent.
    **Context**
    - Existing file: {{existing_document}}
    **Tools**
    - SearchAgent: to gather research.
    - DocsAgent: to consult Obsidian documentation if needed.
    - StyleAgent: to match user tone preferences of existing document.
    - OutlineAgent: to plan before writing.
    - TemplateAgent: if the user requests a specific format (e.g., Blog, Report).
    **Guidelines**:
    - Preserve the original intent of the document while improving clarity and structure.
    - Keep the tone consistent with the existing content (using the 'StyleAgent').
    - Keep the tone informative and concise so it is easy to refine later.
    - Maintain the technical detailing and accuracy of the original document.
    **CRITICAL RULE: DO NOT STOP TO ASK QUESTIONS.**
    **Task**
    1. Read the existing document and understand its content.
    2. Read your instructions and capture the user's intent for the note.
    3. If your research is related to Obsidian, use `docs_tool` to gather specific Obsidian context.
    4. Gather more information using the `search_tool` if needed.
    5. Use the `outline_tool` to structure the gathered information.
    6. Produce a well-structured markdown draft (headings, lists, short paragraphs).
    **Output**
    - Return only the drafted markdown content without explanations or TODO placeholders.""",
    tools=[search_tool, docs_tool, style, outline, template],
    output_key="current_document",
)

# Critic agent provides actionable feedback or signals completion
refinement_edit_critic = LlmAgent(
    name="RefinementEditCritic",
    model=model_pro,
    description="Critique the latest draft and signal when it is good enough.",
    instruction=f"""You review the current draft and decide if additional revisions are necessary.
    **Current Draft**
    {{current_document}}
    **Tools**
    - `LintAgent`: to check for grammar/syntax errors.
    - `StyleAgent`: to verify tone consistency.
    - `ReviewAgent`: to gather overall feedback.
    - `BreakdownAgent`: to understand complex sections needing simplification.
    **CRITICAL RULE: DO NOT STOP TO ASK QUESTIONS.**
    **Task**
    - Evaluate clarity, structure, alignment with the research summary, and overall usefulness.
    - Include tool findings in your critique list.
    - If clear improvements remain, list 1-3 specific, actionable fixes in markdown bullets 
      (e.g., "Clarify the call-to-action").
    **Completion**
    - If the draft already satisfies the request and no major issues remain, respond *exactly* with
      the phrase "{COMPLETION_PHRASE}" and nothing else.
    **Output**
    - Provide either the concise critique list or the exact completion phrase. Do not include commentary beyond that.""",
    tools=[lint, style, review, breakdown],
    output_key="critique_notes",
)

# Refiner either applies the critic's feedback or exits the loop by calling the tool
refinement_edit_writer = LlmAgent(
    name="RefinementEditWriter",
    model=model_pro,
    description="Apply critiques to the draft or exit when the critic signals completion.",
    instruction=f"""You revise the draft using the latest critique.
    **Current Draft**
    {{current_document}}
    **Critique / Suggestions**
    {{critique_notes}}
    **CRITICAL RULE: DO NOT STOP TO ASK QUESTIONS.**
    **Task**
    1. If the critique text matches "{COMPLETION_PHRASE}", call the `exit_loop` tool and output *only* the document without any additional text.
    2. Otherwise, thoughtfully integrate every actionable point while preserving the document's intent and formatting.
    **Output**
    - Return only the improved markdown without summaries or justification.""", 
    tools=[exit_loop],
    output_key="current_document",
)

# LoopAgent executes the critic/writer cycle
refine_edit_agent = LoopAgent(
    name="RefineEditAgent",
    description="Iteratively critique and refine the draft until the critic signals completion or max iterations are reached.",
    sub_agents=[refinement_edit_critic, refinement_edit_writer],
    max_iterations=3,
)


# The updater agent saves the final draft back to the file
updater_agent = LlmAgent(
    name="UpdaterAgent",
    model=model_flash,
    description="Save changes to the existing note.",
    instruction="""Use `update_note` to save the `current_document` edited document back to the file.
    **Current Document**
    {{current_document}}
    **CRITICAL RULE: DO NOT STOP TO ASK QUESTIONS.**
    **Task**:
    - Identify the correct file to update with `list_notes`.
    - Use the `update_note` tool to save the document.""",
    tools=[update_note, list_notes],
    output_key="update_status"
)

# The sequence of loading, rewriting, refining, and updating
existing_content_editor = SequentialAgent(
    name="ExistingContentEditor",
    description="Load existing file content, rewrite and refine iteratively, and save changes.",
    sub_agents=[load_docs_agent, document_rewriter, refine_edit_agent, updater_agent]
)
