from langchain_core.tools import tool

@tool(name_or_callable="create_file_tool", description="Crea archivo en el path, con el contenido")
def create_file_tool(filename: str, content: str) -> str:
    """
    Útil para crear un archivo de texto en el sistema. 
    El usuario debe proporcionar el nombre del archivo y el contenido.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Éxito: El archivo '{filename}' ha sido creado correctamente."
    except Exception as e:
        return f"Error al crear el archivo: {str(e)}"
