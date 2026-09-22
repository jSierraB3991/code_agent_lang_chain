import os
import time
from langchain_core.tools import tool

@tool(name_or_callable="create_directory_tool", description="Crea una nueva carpeta en la ruta especificada.")
def create_directory_tool(path: str) -> dict:
    """
    Crea una nueva carpeta en la ruta especificada.
    
    Args:
        path (str): Ruta de la carpeta a crear. Puede incluir subcarpetas.
        
    Returns:
        dict: Resultado de la operación con estado y detalles
        
    Raises:
        FileExistsError: Si la carpeta ya existe
        PermissionError: Si no hay permisos para crear la carpeta
        OSError: Otros errores del sistema
    """
    
    if not path:
        return {
            'success': False,
            'message': "❌ Error: La ruta proporcionada está vacía",
            'path': path
        }
        
    # Verificar si la carpeta ya existe
    if os.path.exists(path):
        if os.path.isfile(path):
            return {
                'success': False,
                'message': f"❌ Error: '{path}' es un archivo, no una carpeta",
                'path': path
            }
        else:
            return {
                'success': False,
                'message': f"⚠️  Advertencia: La carpeta '{path}' ya existe",
                'path': path,
                'action_taken': None
            }
    
    try:
        os.makedirs(path, mode=0o755)
        
        # Verificar que se creó correctamente
        if not os.path.exists(path):
            return {
                'success': False,
                'message': f"❌ Error: No se pudo crear '{path}' (posible problema de permisos)",
                'path': path
            }
        
        # Obtener información de la carpeta creada
        stat_info = os.stat(path)
        created_time = time.strftime("%H:%M:%S", time.localtime(stat_info.st_ctime))
        
        return {
            'success': True,
            'message': f"✓ Carpeta creada con éxito: {path}",
            'path': path,
            'created_at': created_time,
            'permissions': oct(stat_info.st_mode)[-3:]
        }
        
    except FileExistsError as e:
        return {
            'success': False,
            'message': f"❌ Error: La carpeta '{path}' ya existe",
            'path': path,
            'error': str(e)
        }
        
    except PermissionError as e:
        return {
            'success': False,
            'message': f"❌ Error de permisos al crear '{path}'",
            'path': path,
            'error': str(e),
            'suggestion': "Verifica los permisos del directorio padre o usa sudo si es necesario"
        }
        
    except OSError as e:
        return {
            'success': False,
            'message': f"❌ Error del sistema al crear '{path}'",
            'path': path,
            'error': str(e)
        }

