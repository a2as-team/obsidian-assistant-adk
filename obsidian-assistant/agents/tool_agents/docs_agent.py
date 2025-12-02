"""
This module defines the DocumentationAgent, a specialized LLM agent designed to
consult official Obsidian documentation.

It leverages the `google_search` tool to find information on `help.obsidian.md`,
providing concise explanations and citing sources to answer user questions
about Obsidian features, syntax, and plugins.
"""
from google.adk.agents.llm_agent import LlmAgent
from adk_models import model_flash
from google.adk.tools import google_search

# Obsidian Documentation specialist
docs_agent = LlmAgent(
    name="DocumentationAgent",
    model=model_flash,
    description="Consult official Obsidian documentation for help with features and syntax.",
    instruction="""You are an Obsidian Documentation Specialist.
    **Tools**:
    - `google_search`: Use this tool to search the web for information.
    **Guidelines**:
    - Use `google_search` with the Obsidian Documentation site (help.obsidian.md).
    - Provide concise explanations.
    - Always cite sources.
    **Task**: Search official documentation (help.obsidian.md) to answer questions about Obsidian features, syntax, and plugins.""",
    tools=[google_search],
    output_key="obsidian_documentation"
)