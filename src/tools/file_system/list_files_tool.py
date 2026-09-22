import os
from langchain_core.tools import tool
from libs.constants import dir_no_list, files_no_list

@tool(name_or_callable="list_files_tool", description="Lista todos los archivos en una carpeta específica")
def list_files_tool(directory_path: str) -> str:
    """
    Lista los archivos de una carpeta.
    
    Args:
        directory_path (str): Ruta absoluta o relativa de la carpeta.
    
    Returns:
        list: Lista de nombres de archivos y carpetas
       
    Raises:
        FileNotFoundError: Si el directorio no existe
        PermissionError: Si no hay permisos para leer el directorio
    """
       
    # Validar que el directorio exista
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"El directorio '{directory_path}' no existe")
    
    if not os.path.isdir(directory_path):
        raise IsADirectoryError(f"'{directory_path}' no es un directorio")
    
    try:
        items = os.listdir(directory_path)
        
        # Separar archivos y carpetas para mejor presentación
        dirs = [item for item in items if os.path.isdir(os.path.join(directory_path, item)) and item not in dir_no_list]
        files = [item for item in items if not os.path.isdir(os.path.join(directory_path, item)) and item not in files_no_list]
        
        # Mostrar resultados formateados
        print(f"📂 Directorio: {directory_path}")
        print("=" * 50)
        
        if dirs:
            print("📁 Carpetas:")
            for dir_item in sorted(dirs):
                full_path = os.path.join(directory_path)
                indent = "  │   " 
                print(f"{indent}├── {dir_item}/")
        
        if files:
            print("\n📄 Archivos:")
            for file_item in sorted(files):
                full_path = os.path.join(directory_path, file_item)
                indent = "  │   " 
                size = os.path.getsize(full_path) if os.path.exists(full_path) else 0
                print(f"{indent}├── {file_item} ({size} bytes)")
        
        return ",".join(items)
        
    except PermissionError as e:
        return f"❌ Error de permisos: {e}"
