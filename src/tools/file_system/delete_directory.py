import os
import shutil
from langchain_core.tools import tool

@tool(name_or_callable="delete_directory_tool", description="Elimina una carpeta y todo su contenido del sistema de archivos.")
def delete_directory_tool(directory_path: str) -> str:
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        shutil.rmtree(directory_path)
        return f"Directorio {directory_path} eliminado con éxito."
    else:
        return f"Error: El directorio {directory_path} no existe o no es una carpeta."