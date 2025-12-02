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
from agents.tool_agents.content import summarize_agent, key_points_agent, outline_agent, breakdown_agent

summarize = AgentTool(summarize_agent, 
                           name="summarize_tool", 
                           description="Summarize the content of the target content.", 
                           output_key="summary"
                           )

extract_key_points = AgentTool(key_points_agent, 
                            name="key_points_tool", 
                            description="Extract key points from the target content.", 
                            output_key="key_points"
                            )

outline = AgentTool(outline_agent, 
                         name="outline_tool", 
                         description="Generate an outline from the target content.", 
                         output_key="outline_text"
                         )

breakdown = AgentTool(breakdown_agent, 
                           name="breakdown_tool", 
                           description="Break down complex tasks into actionable subtasks.", 
                           output_key="task_breakdown"
                           )