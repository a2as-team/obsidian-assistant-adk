"""
This module defines the DocumentationAgent and SearchAgent, two specialized LLM agents designed to
consult official Obsidian documentation and perform web research.

The DocumentationAgent leverages the `google_search` tool to find information on `help.obsidian.md`,
providing concise explanations and citing sources to answer user questions
about Obsidian features, syntax, and plugins.

The SearchAgent is designed to find accurate, up-to-date information, synthesize findings
into concise summaries, and cite sources to answer user queries and gather
research.
"""

from google.adk.agents.llm_agent import LlmAgent
from ...adk_models import model_flash, model_pro
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


# Research agent
search_agent = LlmAgent(
    name="SearchAgent", 
    model=model_pro,
    description="Search the web for general information, facts, and research topics.",
    instruction="""You are a Web Research Specialist.
    **Tools**:
    - `google_search`: Use this tool to search the web for information.
    **Guidelines**:
    - Search for accurate, up-to-date information.
    - Synthesize findings into clear, concise summaries.
    - Verify information from multiple sources when possible.
    - Cite sources.
    **Task**: Search the web for accurate information on requested topics.""",
    tools=[google_search],
    output_key="research_summary"
)