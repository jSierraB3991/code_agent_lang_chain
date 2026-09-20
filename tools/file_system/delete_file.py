import os
from langchain_core.tools import tool

@tool(name_or_callable="DeleteFileTool", description="Elimina un archivo del sistema de archivos.")
def delete_file_tool(file_path: str) -> str:
    if os.path.isfile(file_path):
        os.remove(file_path)
        return f"Archivo {file_path} eliminado con éxito."
    else:
        return f"Error: El archivo {file_path} no existe o no es un archivo."