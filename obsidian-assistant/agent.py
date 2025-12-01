from google.adk.agents.llm_agent import Agent
from google.adk.apps.app import App

root_agent = Agent(
    model='gemini-2.5-pro',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)

app = App(
    name="obsidian_assistant",
    root_agent=root_agent,
    # Optionally include App-level features:
    # plugins, context_cache_config, resumability_config
)
