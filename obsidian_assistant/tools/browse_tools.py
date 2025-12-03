"""
This module provides AgentTool definitions for browsing and information retrieval
within the Obsidian Assistant.

It aggregates `search_agent` for general web research and `docs_agent` for
consulting Obsidian-specific documentation, making these functionalities
available as callable tools for other agents.
"""
from google.adk.tools import AgentTool
from ..agents.tool_agents.browse import search_agent, docs_agent

search_tool = AgentTool(agent=search_agent)
docs_tool = AgentTool(agent=docs_agent)