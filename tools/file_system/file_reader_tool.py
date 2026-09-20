from langchain_core.tools import tool

@tool(name_or_callable="FileReaderTool", description="Lee el contenido de un archivo desde el sistema de archivos")
def read_file(filepath: str) -> str:
    """
    Lee el contenido de un archivo y devuelve su texto.
    
    Args:
        filepath (str): La ruta completa del archivo a leer.
    
    Returns:
        str: El contenido del archivo en formato texto.
    """
    # Esta sería la implementación para abrir y leer el archivo
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            return f"Contenido del archivo {filepath}:\n{content}"
    except FileNotFoundError:
        return f"Error: El archivo {filepath} no existe."
    except PermissionError:
        return f"Error: No tienes permisos para leer el archivo {filepath}."
    except Exception as e:
        return f"Error al leer el archivo: {str(e)}"

