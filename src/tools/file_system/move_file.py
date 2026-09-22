import shutil
from langchain_core.tools import tool

@tool(name_or_callable="move_file_tool", description="Mueve un archivo a una nueva ubicación.")
def move_file_tool(source_path: str, destination_path: str) -> str:
    shutil.move(source_path, destination_path)
    return f"Archivo movido de {source_path} a {destination_path}"