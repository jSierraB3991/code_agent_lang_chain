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


def batch_create_directories(paths: list[str], parents: bool = True) -> dict:
    """
    Crea múltiples carpetas en una sola operación.
    
    Args:
        paths (list): Lista de rutas de carpetas a crear
        parents (bool): Crear directorios padres si es necesario
        
    Returns:
        dict: Resumen de todas las operaciones realizadas
    """
    
    results = {
        'total_attempted': len(paths),
        'success_count': 0,
        'failure_count': 0,
        'results': []
    }
    
    for i, path in enumerate(paths, 1):
        print(f"📋 [{i}/{len(paths)}] Procesando: {path}")
        
        result = create_directory(path, parents=parents)
        results['results'].append({
            'path': path,
            'result': result
        })
        
        if result['success']:
            results['success_count'] += 1
            print(f"   ✓ {result['message']}")
        else:
            results['failure_count'] += 1
            print(f"   ✗ {result['message']}")
    
    return results


def create_directory_tree(path: str, parents: bool = True) -> dict:
    """
    Crea una estructura de directorio jerárquica completa.
    
    Args:
        path (str): Ruta base del árbol a crear
        parents (bool): Crear todos los niveles necesarios
        
    Returns:
        dict: Información sobre el árbol creado
    """
    
    # Crear todos los directorios padres automáticamente
    result = create_directory(path, parents=parents)
    
    if not result['success']:
        return result
    
    # Listar lo que se creó
    created_items = []
    current_path = path.strip(os.sep)
    level = 0
    
    # Recorrer el árbol hasta encontrar archivos existentes
    while os.path.dirname(current_path):
        parent = os.path.dirname(current_path)
        if not os.path.exists(parent):
            break
        current_path = parent
        
        # Construir nombre completo del directorio
        full_path = current_path
    
    return {
        'path': path,
        'message': f"✓ Árbol de carpetas creado: {path}",
        'success': True,
        'created_tree': str(current_path)
    }

