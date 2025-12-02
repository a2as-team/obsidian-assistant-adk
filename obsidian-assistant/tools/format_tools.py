"""
This module provides AgentTool definitions for various formatting tasks
within the Obsidian Assistant.

It aggregates `lint_agent` for ensuring proper markdown syntax, `template_agent`
for applying structured templates, and `style_agent` for rewriting content
to match a specific style. These tools make the underlying formatting agents
available as callable functions for other agents.
"""
from google.adk.tools import AgentTool
from agents.tool_agents.format_agents import lint_agent, template_agent, style_agent

lint = AgentTool(lint_agent, 
                 name="lint_tool", 
                 description="Lint markdown content to ensure proper syntax.", 
                 output_key="linted_markdown"
                 )
template = AgentTool(template_agent, 
                     name="template_tool", 
                     description="Apply a given template to raw markdown content.", 
                     output_key="templated_content"
                     )
style = AgentTool(style_agent, 
                  name="style_tool", 
                  description="Rewrite content to match a reference style file.", 
                  output_key="styled_content"
                  )