"""
This module provides a set of AgentTool definitions for various content
processing tasks within the Obsidian Assistant.

It includes tools for:
- `summarize`: To condense text into concise summaries.
- `extract_key_points`: To extract actionable key insights from content.
- `outline`: To generate structured hierarchical outlines.
- `breakdown`: To decompose complex tasks into actionable subtasks and checklists.
These tools make the underlying content processing agents available as callable
functions for other agents, facilitating content creation, analysis, and organization.
"""

from google.adk.tools import AgentTool
from ..agents.tool_agents.content import summarize_agent, key_points_agent, outline_agent, breakdown_agent

summarize = AgentTool(agent=summarize_agent)

extract_key_points = AgentTool(agent=key_points_agent)

outline = AgentTool(agent=outline_agent)
                       

breakdown = AgentTool(agent=breakdown_agent)