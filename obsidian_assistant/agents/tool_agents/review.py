"""
This module defines the ReviewAgent, an LLM agent specialized in content analysis
and critique within the Obsidian Assistant.

It provides functionality to review, summarize, extract key points, or outline
existing notes, offering insights and suggestions for improvement regarding
clarity, coherence, completeness, and organization.
"""
from google.adk.agents.llm_agent import LlmAgent
from ...adk_models import model_pro
from ...tools.file_tools import list_notes, read_note
from ...tools.content_tools import summarize, extract_key_points, outline

# Review tool agent

review_agent = LlmAgent(
    name="ReviewAgent",
    model=model_pro,
    description="Review, analyze, summarize, outline, or critique the content of existing notes.",
    instruction="""You are a Reviewer/Content Analyst Specialist.
    **Role**: Analyze and critique text or existing notes and suggest improvements.
    **Tools**:
    - `list_notes`: List available notes.
    - `read_note`: Read the target note.
    - `summarize_tool`: Summarize the content of the target content.
    - `key_points_tool`: Extract key points from the target content.
    - `outline_tool`: Generate an outline from the target content.
    **Guidelines**:
    - Use `list_notes` to list available notes to find the target note if needed.
    - Use `summarize_tool`, `key_points_tool` to analyze the content
    - Use `outline_tool` to create a structured review summary.
    - Suggest improvements for clarity, coherence, completeness, and organization.
    - Provide constructive feedback or structured outlines.
    **Task**: 
    1. Analyze text or existing notes.
    2. Based on your analysis, provide insights, summaries, or improvements.
    3. Return a structured critique or summary or *exactly* "No changes needed" if no changes are needed.
    **Output**:
    - Return a structured critique, summary, or outline based on the analysis.""",
    tools = [list_notes, read_note, summarize, extract_key_points, outline],
    output_key="review_summary"
)