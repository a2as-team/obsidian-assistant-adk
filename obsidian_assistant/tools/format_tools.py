"""
This module provides AgentTool definitions for various formatting tasks
within the Obsidian Assistant.

It aggregates `lint_agent` for ensuring proper markdown syntax, `template_agent`
for applying structured templates, and `style_agent` for rewriting content
to match a specific style. These tools make the underlying formatting agents
available as callable functions for other agents.
"""
from google.adk.tools import AgentTool
from ..agents.tool_agents.format import lint_agent, template_agent, style_agent

lint = AgentTool(agent=lint_agent)
template = AgentTool(agent=template_agent)
style = AgentTool(agent=style_agent)