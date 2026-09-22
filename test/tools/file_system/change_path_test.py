import unittest
import os
from src.tools.file_system.change_path import change_path_tool

class TestChangePath(unittest.TestCase):
    def setUp(self):
        # Guardar la ruta inicial para volver a ella después de cada test
        self.initial_path = os.path.abspath(os.getcwd())

    def tearDown(self):
        # Asegurarse de volver a la ruta original después de cada test
        os.chdir(self.initial_path)

    def test_change_path_to_src_and_back(self):
        # Caso 1: Cambiar a ./src
        # Guardamos la ruta absoluta esperada para evitar problemas con rutas relativas
        expected_src_path = os.path.abspath("src")
        
        # Primer cambio: a ./src
        result1 = change_path_tool.invoke("src")
        # Verificamos que el directorio de trabajo sea el correcto. 
        # Como la herramienta retorna un string, validamos contra la lógica interna.
        self.assertIn("Cambiado al directorio:", result1)
        self.assertEqual(os.path.abspath(os.getcwd()), expected_src_path)

        # Caso 2: Volver atrás con ./../
        result2 = change_path_tool.invoke("../")
        self.assertIn("Cambiado al directorio:", result2)
        # Verificamos que haya vuelto al directorio original
        self.assertEqual(os.path.abspath(os.getcwd()), self.initial_path)

if __name__ == "__main__":
    unittest.main()
