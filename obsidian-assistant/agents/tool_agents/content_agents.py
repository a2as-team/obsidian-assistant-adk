"""
This module provides a collection of specialized agents for various content
processing tasks within the Obsidian Assistant.

It includes:
- `SummarizeAgent`: For condensing text into concise summaries.
- `KeyPointsAgent`: For extracting actionable key insights from content.
- `OutlineAgent`: For generating structured hierarchical outlines.
- `BreakdownAgent`: For decomposing complex tasks into actionable subtasks and checklists.
These agents are designed to assist in content creation, analysis, and organization
within the knowledge base.
"""
from google.adk.agents.llm_agent import LlmAgent
from adk_models import model_flash, model_flash_lite

summarize_agent = LlmAgent(
    name="SummarizeAgent",
    model=model_flash_lite,
    description="Condense text into concise summaries with `max_length` (short, medium, long, or custom lines/characters).",
    instruction="""You are a summarization specialist.
    **Guidelines**:
    - Read the provided `content` and capture the main ideas and key information.
    - Respect the `max_length` argument (short, medium, long, or custom lines/characters).
    **Task**:
    - Generate a concise summary based on the `content` and specified `max_length`.
    **Output**:
    - Return only the summary text in markdown form.
    - Do not add prefaces, metadata, or analysis beyond the summary.""",
    output_key="summary",
)

key_points_agent = LlmAgent(
    name="KeyPointsAgent",
    model=model_flash_lite,
    description="Extract actionable key points from source material using `num_points` distinct insights.",
    instruction="""You identify the most important points in the supplied `content`.
    **Guidelines**:
    - Extract up to `num_points` distinct insights.
    - Preserve factual accuracy and original intent.
    **Task**:
    1. Identify all key points in the content.
    2. Extract the most relevant `num_points` distinct insights from all key points in the content.
    **Output**:
    - Return a numbered markdown list of the extracted points.
    - Keep each point concise and self-contained.""",
    output_key="key_points",
)

outline_agent = LlmAgent(
    name="OutlineAgent",
    model=model_flash,
    description="Generate structured outlines from notes or research with different levels of depth.",
    instruction="""You create hierarchical outlines from the given `content`.
    **Guidelines**:
    - Respect the requested depth (e.g., 1-level, 2-level, or 3-level headings).
    - Capture the logical flow of the source material while staying faithful to the text.
    **Task**:
    - Produce an outline based on the `content` and specified depth.
    **Output**:
    - Return markdown headings (e.g., #, ##, ###, -) representing the outline only.
    - Do not include prose explanations outside of the outline.""",
    output_key="outline_text",
)

breakdown_agent = LlmAgent(
    name="BreakdownAgent",
    model=model_flash,
    description="Break complex tasks into actionable subtasks and checklists with different levels of granularity.",
    instruction="""You decompose task description inputs into smaller steps.
    **Guidelines**:
    - Interpret if granularity (e.g. high, medium, low) is requested to control detail.
    - Focus on creating manageable, ordered subtasks that covers the original request.
    **Task**:
    1. Understand the overall task description.
    2. If provided granularity, determine the level of detail needed.
    3. Break down the task into clear, actionable subtasks.
    - Generate a checklist of subtasks based on the task description and granularity.
    **Output**:
    - Return an actionable checklist in markdown using `- [ ]` syntax.
    - Keep each checkbox specific and outcome-oriented.""",
    output_key="task_breakdown",
)