import string
import random
import sys
import subprocess
import argparse
from model.arguments import Arguments
from .constants import MODEL, THREAD_ID

def random_string() ->str:
    caracteres = string.ascii_letters + string.digits 
    longitud = 15
    cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(longitud))
    return cadena_aleatoria

def clear_screen():
    subprocess.run(['cls'] if sys.platform == 'win32' else ['clear'])

def stop_model(model: str):
    #subprocess.run(["ollama", "stop", model])
    print(f"Stop model {model}")


def process_args() -> Arguments:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "project",
        nargs="?",
        default=".",
        help="Ruta del proyecto"
    )
    parser.add_argument(
        "-p", "--project",
        dest="project_option",
        help="Ruta del project"
    )
    parser.add_argument(
        "-m", "--model",
        default=MODEL,
        help="Modelo de Ollama"
    )
    args = parser.parse_args()
    project = args.project_option or args.project
    if not project:
        parser.error("Debes especificar el proyecto")
    print(f"Proyecto: {project}")
    print(f"Modelo: {args.model}")
    return Arguments(project=project, model=args.model, thread_id=THREAD_ID)