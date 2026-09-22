import os
import sys
import subprocess

from langchain_core.tools import tool


@tool(
    name_or_callable="run_python_tests_tool",
    description="Ejecuta los tests de Python usando pytest en el path especificado."
)
def run_python_tests_tool(path: str) -> str:
    """
    Ejecuta pytest en la carpeta indicada.

    Args:
        path: Ruta de la carpeta donde están los tests.

    Returns:
        Resultado completo de pytest.
    """

    if not os.path.isdir(path):
        return f"Error: el directorio '{path}' no existe o no es una carpeta."

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "."],
            cwd=path,
            capture_output=True,
            text=True,
            check=False,
        )

        output = []

        if result.stdout:
            output.append(result.stdout.rstrip())

        if result.stderr:
            output.append(result.stderr.rstrip())

        if result.returncode == 0:
            output.append("Tests de Python: PASADOS")
        else:
            output.append(
                f"Tests de Python: FALLARON (exit code: {result.returncode})"
            )

        return "\n".join(output)

    except Exception as e:
        return f"Error al ejecutar los tests: {e}"