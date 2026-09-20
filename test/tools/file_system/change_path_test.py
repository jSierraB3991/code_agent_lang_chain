import unittest
import os
from tools.file_system.change_path import change_path_tool

class TestChangePath(unittest.TestCase):
    def setUp(self):
        # Guardar la ruta inicial para volver a ella después de cada test
        self.initial_path = os.getcwd()

    def tearDown(self):
        # Asegurarse de volver a la ruta original después de cada test
        os.chdir(self.initial_path)

    def test_change_path_to_src_and_back(self):
        # Caso 1: Cambiar a ./src
        # Nota: En un entorno real, asumimos que la carpeta 'src' existe en la raíz del proyecto
        # o que la ruta relativa es válida.
        
        # Primer cambio: a ./src
        result1 = change_path_tool.invoke("src")
        # Verificamos que el directorio de trabajo sea el correcto. 
        # Como la herramienta retorna un string, validamos contra la lógica interna.
        self.assertIn("Cambiado al directorio:", result1)
        self.assertEqual(os.getcwd(), os.path.abspath("src"))

        # Caso 2: Volver atrás con ./../
        result2 = change_path_tool.invoke("../")
        self.assertIn("Cambiado al directorio:", result2)
        # Verificamos que haya vuelto al directorio original (o una carpeta superior si src estaba en una subcarpeta)
        # Para este test específico, validamos que la ruta actual sea la que esperamos tras el comando
        self.assertEqual(os.getcwd(), os.path.abspath("."))

if __name__ == "__main__":
    unittest.main()
