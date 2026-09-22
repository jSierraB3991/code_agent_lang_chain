from pathlib import Path
from langchain_core.tools import tool


@tool(
    name_or_callable="create_file_tool",
    description="Crea un archivo en el path indicado. Si no se especifica path, utiliza el directorio actual."
)
def create_file_tool(
    filename: str,
    content: str,
    path: str = "."
) -> str:
    """
    Crea un archivo en el directorio indicado.

    Args:
        filename: Nombre del archivo a crear.
        content: Contenido del archivo.
        path: Directorio donde crear el archivo. Por defecto, ".".
    """
    try:
        file_path = Path(path) / filename

        with file_path.open("w", encoding="utf-8") as f:
            f.write(content)

        return f"Éxito: El archivo '{file_path}' ha sido creado correctamente."

    except Exception as e:
        return f"Error al crear el archivo: {e}"