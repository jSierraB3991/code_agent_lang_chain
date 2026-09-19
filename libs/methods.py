import string
import random
import sys
import subprocess

def random_string() ->str:
    caracteres = string.ascii_letters + string.digits 
    longitud = 15
    cadena_aleatoria = ''.join(random.choice(caracteres) for _ in range(longitud))
    return cadena_aleatoria

def clear_screen():
    subprocess.run(['cls'] if sys.platform == 'win32' else ['clear'])
