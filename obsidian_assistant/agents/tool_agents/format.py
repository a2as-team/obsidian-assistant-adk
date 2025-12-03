"""
This module provides a suite of LLM agents designed for various markdown formatting
tasks within the Obsidian Assistant.

It includes:
- `LintAgent`: Ensures markdown content adheres to proper syntax and formatting.
- `TemplateAgent`: Applies a given structured template to raw markdown content.
- `StyleAgent`: Rewrites content to match a specified reference style or tone.
These agents facilitate the creation and maintenance of consistently formatted
and styled documentation within the knowledge base.
"""
from google.adk.agents.llm_agent import LlmAgent
from ...adk_models import model_flash
from ...tools.file_tools import list_notes, read_note

lint_agent = LlmAgent(
    name="LintAgent",
    model=model_flash,
    description="Ensure markdown adheres to proper syntax.",
    instruction="""You lint markdown content.
    **Guidelines**:
    - Inspect the provided content for syntax errors or malformed structures.
    - Fix heading levels, code blocks, lists, and spacing as needed without altering meaning.
    **Task**:
    - Inspect and correct the markdown syntax in the provided content.
    **Output**:
    - Return ONLY the corrected markdown.
    - Do not add explanations or commentary.""",
    output_key="linted_markdown",
)

template_agent = LlmAgent(
    name="TemplateAgent",
    model=model_flash,
    description="Apply structured given template to raw markdown content.",
    instruction="""You remodel content so it follows a given template.
    **Guidelines**:
    - Preserve the original ideas and facts.
    - Map sections of the content into the template structure, filling placeholders as needed.
    **Task**:
    - Apply the template to the content, ensuring all sections are appropriately filled.
    **Output**:
    - Return the fully formatted markdown following the template.
    - Exclude any reasoning steps or notes.""",
    output_key="templated_content",
)

style_agent = LlmAgent(
    name="StyleAgent",
    model=model_flash,
    description="Rewrite content so it matches a reference style file.",
    instruction="""You adapt tone, formatting, and voice to match a reference note.
    **Tools**:
    - `list_notes`: List available notes to find the style file if a file name is misspelled.
    - `read_note`: Read the style file to understand its conventions.
    **Guidelines**:
    - Follow the structure and formatting of the reference note if provided.
    - Maintain the original meaning and context while adapting the style.
    - Use `list_notes` and `read_note` to access the style file.
    **Task**:
    Case A (receive a file name):
    1. Read the example style using `read_note(style_file)`.
    2. Mirror the example's cadence, vocabulary, and markdown conventions without copying sentences 
    verbatim in the target content.
    Case B (no style file, example content provided):
    1. Read the provided `example_content` if no style file is given.
    2. Mirror the example's cadence, vocabulary, and markdown conventions without copying sentences 
    verbatim in the target content.
    Case C (style description provided):
    1. Understand the overall style description intent.
    2. Use the provided style description to adapt the content.
    **Output**:
    - Return only the rewritten content in the new style.
    - If the style file cannot be read, explain the issue and request a valid file name.""",
    tools=[list_notes, read_note],
    output_key="styled_content",
)