# Test file for delete_directory.py
import unittest
import os
import shutil
from tools.file_system.delete_directory import delete_directory_tool

class TestDeleteDirectory(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory and a nested structure
        self.test_dir = "test_delete_dir"
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        
        # Create a file inside the directory
        self.file_path = os.path.join(self.test_dir, "test_file.txt")
        with open(self.file_path, "w") as f:
            f.write("some content")
            
        # Create a subdirectory
        self.sub_dir = os.path.join(self.test_dir, "sub_dir")
        os.makedirs(self.sub_dir)
        with open(os.path.join(self.sub_dir, "sub_file.txt"), "w") as f:
            f.write("sub content")

    def tearDown(self):
        # Clean up the directory if it exists
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_delete_directory_success(self):
        # Test successful deletion
        result = delete_directory_tool(self.test_dir)
        self.assertIn("eliminado con éxito", result)
        self.assertFalse(os.path.exists(self.test_dir))

    def test_delete_directory_not_exists(self):
        # Test deletion of non-existent directory
        result = delete_directory_tool("non_existent_directory_999")
        self.assertIn("Error: El directorio", result)
        self.assertIn("no existe", result)

    def test_delete_directory_not_a_directory(self):
        # Test trying to delete a file as if it were a directory
        file_path = os.path.join(self.test_dir, "some_file.txt")
        result = delete_directory_tool(file_path)
        self.assertIn("Error: El directorio", result)
        self.assertIn("no es una carpeta", result)

if __name__ == "__main__":
    unittest.main()
