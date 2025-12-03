"""
This module provides AgentTool definitions for writing and reviewing content
within the Obsidian Assistant.

It aggregates `quick_logger_agent` for quickly creating, appending, or updating
notes, and `review_agent` for analyzing and critiquing content. These tools
make the underlying agents available as callable functions for other agents.
"""
from google.adk.tools import AgentTool
from ..agents.tool_agents.quick_log import quick_logger_agent
from ..agents.tool_agents.review import review_agent

quick_log = AgentTool(agent=quick_logger_agent)
review = AgentTool(agent=review_agent)