import os
from langchain_core.tools import tool

@tool(name_or_callable="change_path_tool", description="Cambia el directorio de trabajo actual del sistema.")
def change_path_tool(path: str) -> str:
    os.chdir(path)
    return f"Cambiado al directorio: {os.getcwd()}"