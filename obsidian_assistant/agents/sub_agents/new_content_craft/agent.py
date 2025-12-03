"""
This module defines a multi-agent system for crafting new content within the
Obsidian Assistant.

It comprises several specialized agents:
- `ResearchDraftWriter`: Creates the initial draft based on research.
- `RefinementCritic`: Critiques the draft and provides actionable feedback.
- `RefinementWriter`: Applies the feedback to refine the draft.
- `RefineAgent`: Manages the iterative critique and refinement loop.
- `PublishAgent`: Publishes the final, refined document as a new note.
The `NewContentCrafter` orchestrates these agents to provide a robust
and iterative content creation workflow, from research to publication.
"""

from google.adk.agents import LlmAgent, SequentialAgent, LoopAgent
from google.adk.tools import ToolContext
from ....adk_models import model_pro, model_flash
from ....tools.file_tools import create_note
from ....tools.browse_tools import search_tool
from ....tools.content_tools import outline, breakdown
from ....tools.format_tools import style, lint, template
from ....tools.write_tools import review

COMPLETION_PHRASE = "No major issues found."

def exit_loop(tool_context: ToolContext):
  """Call only when the critic responds with the completion phrase to stop the refinement loop."""
  print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
  tool_context.actions.escalate = True
  return {}

# Initial writer produces the first draft that the loop will iteratively improve
research_draft_writer = LlmAgent(
    name="ResearchDraftWriter",
    model=model_pro,
    description="Create the first markdown draft using research context.",
    instruction="""You are the Draft Writer Specialist for the Obsidian Agent.
    **Tools**:
    - Use `SearchAgent` tool to gather research.
    - Use the `OutlineAgent` tool to plan before writing.
    - Use the `TemplateAgent` tool if the user requests a specific format (e.g., Blog, Report).
    **CRITICAL RULE: DO NOT STOP TO ASK QUESTIONS.**
    **Task**:
    1. Gather relevant research using the `SearchAgent` tool.
    2. Read the research summary and capture the user's intent for the note.
    3. Produce a well-structured markdown draft (headings, lists, short paragraphs) that covers the critical points.
    4. Keep the tone informative and concise so it is easy to refine later.
    **Output**:
    Return only the drafted markdown content without explanations or TODO placeholders.""",
    tools=[outline, template, search_tool],
    output_key="current_document",
)

# Critic agent provides actionable feedback or signals completion
refinement_critic = LlmAgent(
    name="RefinementCritic",
    model=model_pro,
    description="Critique the latest draft and signal when it is good enough.",
    instruction=f"""You review the current draft and decide if additional revisions are necessary.
    **Current Draft**
    {{current_document}}
    **Tools**
    - Use the `lint_tool` to check for grammar/syntax errors.
    - Use the `style_tool` to verify tone consistency.
    - Use the `review_tool` to gather overall feedback.
    - Use the `breakdown_tool` to identify complex sections needing simplification.
    **Task**
    - Evaluate clarity, structure, alignment with the research summary, and overall usefulness.
    - Include tool findings in your critique list.
    - If clear improvements remain, list 1-3 specific, actionable fixes in markdown bullets 
    (e.g., "Clarify the call-to-action").
    **CRITICAL RULE: DO NOT STOP TO ASK QUESTIONS.**
    **Completion**
    - If the draft already satisfies the request and no major issues remain, respond *exactly* with 
    the phrase "{COMPLETION_PHRASE}" and nothing else.
    **Output**
    - Provide either the concise critique list or the exact completion phrase. Do not include commentary beyond that.""",
    tools=[lint, style, review, breakdown],
    output_key="critique_notes",
)

# Refiner either applies the critic's feedback or exits the loop by calling the tool
refinement_writer = LlmAgent(
    name="RefinementWriter",
    model=model_flash,
    description="Apply critiques to the draft or exit when the critic signals completion.",
    instruction=f"""You revise the draft using the latest critique.
    **Current Draft**
    {{current_document}}
    **Critique / Suggestions**
    {{critique_notes}}
    **CRITICAL RULE: DO NOT STOP TO ASK QUESTIONS.**
    **Task**
    1. If the critique text matches "{COMPLETION_PHRASE}", call the `exit_loop` tool and output *only* 
    the document without any additional text.
    2. Otherwise, thoughtfully integrate every actionable point while preserving the document's intent and formatting.
    **Output**
    - Return only the improved markdown without summaries or justification.""",
    tools=[exit_loop],
    output_key="current_document",
)

# Publisher agent saves the final draft into the vault
publish_agent = LlmAgent(
    name="PublishAgent",
    model=model_flash,
    description="Publish the draft in a new note in the user's vault.",
    instruction="""You save the current document into the user's Obsidian vault.
    **Current Document**
    {{current_document}}
    **CRITICAL RULE: DO NOT STOP TO ASK QUESTIONS.**
    **Task**:
    - Use the `create_note` tool to save the document.""",
    tools=[create_note],
    output_key="publication_status",
)

# LoopAgent executes the critic/writer cycle
refine_agent = LoopAgent(
    name="RefineAgent",
    description="Iteratively critique and refine the draft until the critic signals completion or max iterations are reached.",
    sub_agents=[refinement_critic, refinement_writer],
    max_iterations=3,
)

# Sequential workflow: gather research, create the initial draft, then run refinement loop, and publish
new_content_crafter = SequentialAgent(
    name="NewContentCrafter",
    description="Run research, draft the note, then refine iteratively using the critic/writer loop.",
    sub_agents=[research_draft_writer, refine_agent, publish_agent]
)

