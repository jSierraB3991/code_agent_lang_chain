# Test file for list_files_tool.py
import unittest
import os
import shutil
from src.tools.file_system.list_files_tool import list_files_tool

class TestListFiles(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = "test_list_dir"
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
        
        # Create some files and subdirectories
        self.file1 = os.path.join(self.test_dir, "file1.txt")
        with open(self.file1, "w") as f:
            f.write("content1")
        
        self.sub_dir = os.path.join(self.test_dir, "sub_dir")
        os.makedirs(self.sub_dir)
        
        self.file2 = os.path.join(self.sub_dir, "file2.txt")
        with open(self.file2, "w") as f:
            f.write("content2")

    def tearDown(self):
        # Remove the temporary directory and its contents
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_list_files_success(self):
        result = list_files_tool.invoke(self.test_dir)
        # Check if files and directories are in the result
        self.assertIn("file1.txt", result)
        self.assertIn("sub_dir", result)

    def test_list_files_not_found(self):
        with self.assertRaises(FileNotFoundError):
            list_files_tool.invoke(f"{self.test_dir}/file_no_found.txt")

    def test_list_files_is_directory(self):
        with self.assertRaises(IsADirectoryError):
            list_files_tool.invoke(f"{self.test_dir}/file1.txt")
            
        # Create a file and try to list it as a directory
        file_path = os.path.join(self.test_dir, "some_file.txt")
        with open(file_path, "w") as f:
            f.write("test")
        with self.assertRaises(IsADirectoryError):
            list_files_tool.invoke(file_path)

if __name__ == "__main__":
    unittest.main()
