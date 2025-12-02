"""
This module provides AgentTool definitions for writing and reviewing content
within the Obsidian Assistant.

It aggregates `quick_logger_agent` for quickly creating, appending, or updating
notes, and `review_agent` for analyzing and critiquing content. These tools
make the underlying agents available as callable functions for other agents.
"""
from google.adk.tools import AgentTool
from agents.tool_agents import quick_logger_agent, review_agent

quick_log = AgentTool(quick_logger_agent, 
                            name="quick_log_tool", 
                            description="Quickly log notes or snippets.", 
                            output_key="logged_content"
                            )

review = AgentTool(review_agent, 
                        name="review_tool", 
                        description="Review and provide feedback on notes.", 
                        output_key="reviewed_content"
                        )