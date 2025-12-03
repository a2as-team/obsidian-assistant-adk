"""
This module defines the SearchAgent, an LLM agent specialized in performing
web research using Google Search.

It is designed to find accurate, up-to-date information, synthesize findings
into concise summaries, and cite sources to answer user queries and gather
research.
"""
from google.adk.agents.llm_agent import LlmAgent
from ...adk_models import model_pro
from google.adk.tools import google_search

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