"""
This module provides a set of tools for interacting with markdown files in an Obsidian vault.

It includes functions for creating, reading, updating, deleting, and listing notes,
as well as appending content to existing notes and merging notes. These functions
are intended to be used as tools by an ADK agent.
"""
import os
from ..config import load_settings

settings = load_settings()
vault_path = settings.vault_path

def create_note(filename: str, content: str) -> dict:
    """Creates a new markdown note in the vault.
    
    Args:
        filename: The name of the file (e.g., 'Meeting Notes.md'). 
                  If .md is missing, it will be added.
        content: The text content to write into the note.
        
    Returns:
        A dictionary indicating success or failure.
    """
    if not filename.endswith(".md"):
        filename += ".md"
        
    filepath = os.path.join(vault_path, filename)
    
    try:
        with open(filepath, "w") as f:
            f.write(content)
        return {"status": "success", "message": f"Note '{filename}' created successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def read_note(filename: str) -> dict:
    """Reads the content of an existing markdown note.
    
    Args:
        filename: The name of the file to read.
        
    Returns:
        The content of the note or an error message.
    """
    if not filename.endswith(".md"):
        filename += ".md"
        
    filepath = os.path.join(vault_path, filename)
    
    if not os.path.exists(filepath):
        return {"status": "error", "message": f"Note '{filename}' does not exist."}
        
    try:
        with open(filepath, "r") as f:
            content = f.read()
        return {"status": "success", "content": content}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def update_note(filename: str, content: str) -> dict:
    """Updates the content of an existing markdown note.
    
    Args:
        filename: The name of the file.
        content: The new text content to write into the note.
        
    Returns:
        A dictionary indicating success or failure.
    """
    if not filename.endswith(".md"):
        filename += ".md"
        
    filepath = os.path.join(vault_path, filename)
    
    if not os.path.exists(filepath):
        return {"status": "error", "message": f"Note '{filename}' does not exist."}
        
    try:
        with open(filepath, "w") as f:
            f.write(content)
        return {"status": "success", "message": f"Note '{filename}' updated successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def delete_note(filename: str) -> dict:
    """Deletes an existing markdown note.
    
    Args:
        filename: The name of the file to delete.
        
    Returns:
        A dictionary indicating success or failure.
    """
    if not filename.endswith(".md"):
        filename += ".md"
        
    filepath = os.path.join(vault_path, filename)
    
    if not os.path.exists(filepath):
        return {"status": "error", "message": f"Note '{filename}' does not exist."}
        
    try:
        os.remove(filepath)
        return {"status": "success", "message": f"Note '{filename}' deleted successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def list_notes() -> list[str]:
    """Lists all markdown notes in the vault.
    
    Returns:
        A list of filenames in the vault.
    """
    try:
        return [f for f in os.listdir(vault_path) if f.endswith(".md")]
    except Exception as e:
        return {"status": "error", "message": str(e)}
    

def append_to_note(filename: str, content: str) -> dict:
    """Appends content to an existing markdown note.
    
    Args:
        filename: The name of the file.
        content: The text content to append.
        
    Returns:
        A dictionary indicating success or failure.
    """
    if not filename.endswith(".md"):
        filename += ".md"
        
    filepath = os.path.join(vault_path, filename)
    
    if not os.path.exists(filepath):
        return {"status": "error", "message": f"Note '{filename}' does not exist."}
        
    try:
        with open(filepath, "a") as f:
            f.write("\n" + content)
        return {"status": "success", "message": f"Content appended to '{filename}' successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
def merge_notes(source_filename: str, target_filename: str) -> dict:
    """Merges content from source note into target note.
    
    Args:
        source_filename: The name of the source file.
        target_filename: The name of the target file.

    Returns:
        A dictionary indicating success or failure.
    """
    if not source_filename.endswith(".md"):
        source_filename += ".md"
    if not target_filename.endswith(".md"):
        target_filename += ".md"

    source_filepath = os.path.join(vault_path, source_filename)
    target_filepath = os.path.join(vault_path, target_filename)

    if not os.path.exists(source_filepath):
        return {"status": "error", "message": f"Source note '{source_filename}' does not exist."}
    if not os.path.exists(target_filepath):
        return {"status": "error", "message": f"Target note '{target_filename}' does not exist."}

    try:
        with open(source_filepath, "r") as source_file:
            source_content = source_file.read()
        with open(target_filepath, "a") as target_file:
            target_file.write("\n" + source_content)
        return {"status": "success", "message": f"Note '{source_filename}' merged into '{target_filename}' successfully."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Aggregate File Interaction Tools
file_tools = [ 
    create_note,
    read_note,
    update_note,
    delete_note,
    list_notes,
    append_to_note,
    merge_notes,
]
