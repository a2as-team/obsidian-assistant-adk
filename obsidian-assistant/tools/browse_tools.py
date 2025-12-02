"""
This module provides AgentTool definitions for browsing and information retrieval
within the Obsidian Assistant.

It aggregates `search_agent` for general web research and `docs_agent` for
consulting Obsidian-specific documentation, making these functionalities
available as callable tools for other agents.
"""
from google.adk.tools import AgentTool
from agents.tool_agents import search_agent, docs_agent

search_tool = AgentTool(search_agent,
                          name="google_search_tool",
                          description="Search the web for general information, facts, and research topics.",
                          output_key="research_summary"
                          )
docs_tool = AgentTool(docs_agent,
                        name="obsidian_docs_tool",  
                        description="Access and retrieve documents from the Obsidian vault.",
                        output_key="document_summary"
                        )