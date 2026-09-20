import subprocess
import os
from langchain_core.tools import tool

@tool(name_or_callable="run_go_tests_tool", description="Herramienta para poder correr los test en proyectos de golang")
def run_go_tests_tool(path):
    if not os.path.exists(path):
        print(f"Error: El directorio {path} no existe.")
        return
    
    print(f"Ejecutando tests de Go en: {path}")
    try:
        # Ejecuta 'go test ./...' en el directorio especificado
        subprocess.run(["go", "test", "./..."], cwd=path, check=False)
    except FileNotFoundError:
        print("Error: No se pudo ejecutar 'go'. Asegúrate de que Go esté instalado.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar tests de Go: {e}")
