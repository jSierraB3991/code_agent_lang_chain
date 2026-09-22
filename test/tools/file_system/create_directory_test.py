import unittest
import pytest
import os
import shutil
from src.tools.file_system.create_directory import create_directory_tool


class TestCreateDirectory(unittest.TestCase):
    """Pruebas para la función create_directory"""

    def setUp(self):
        self.test_dir = "test_tools"

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_crear_carpeta_exitosa(self):
        """Test de creación exitosa de una carpeta"""
        path = "test_tools/file_system/test_create_dir"
        result = create_directory_tool.invoke(path)
        
        assert result['success'] is True
        assert 'Carpeta creada con éxito' in result['message']
        assert result['path'] == path

    def test_carpeta_que_ya_existe(self):
        """Test cuando la carpeta ya existe"""
        # Primero creamos la carpeta
        path = "test_tools/file_system/test_already_exists"
        create_directory_tool.invoke(path)
        
        # Ahora intentamos crearla de nuevo
        result = create_directory_tool.invoke(path)
        
        assert result['success'] is False
        assert 'ya existe' in result['message'].lower()

    def test_ruta_vacia(self):
        """Test con ruta vacía"""
        result = create_directory_tool.invoke("")
        
        assert result['success'] is False
        assert "vacía" in result['message']

    def test_carpeta_con_subcarpetas(self):
        """Test de creación de carpetas anidadas"""
        path = "test_tools/file_system/nested/dir1/dir2/dir3"
        result = create_directory_tool.invoke(path)
        
        assert result['success'] is True
        assert 'Carpeta creada con éxito' in result['message']

    def test_crear_archivo_en_lugar_de_carpeta(self):
        """Test de intentar crear carpeta donde hay un archivo"""
        # Crear un archivo primero
        create_directory_tool.invoke("test_tools/file_system/")
        
        with open("test_tools/file_system/test_file.txt", "w") as f:
            f.write("contenido")
        
        result = create_directory_tool.invoke("test_tools/file_system/test_file.txt")
        
        assert result['success'] is False
        assert "archivo" in result['message'].lower()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
