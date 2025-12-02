"""
This module serves as the main entry point for the Obsidian Assistant ADK application.

It initializes the ADK App, sets up the root agent, and configures the overall
application behavior.
"""
from google.adk.apps.app import App
from agents.root_agent import agent

app = App(
    name="obsidian_assistant",
    root_agent=agent,
    # Optionally include App-level features:
    # plugins, context_cache_config, resumability_config
)