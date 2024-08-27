import os
import shutil
import unittest

import file_ninja.file_manager as file_manager


class CopyFileTest(unittest.TestCase):
    def setUp(self):
        self.temp_filepath = "/tmp/file_ninja_tests/"
        if not os.path.exists(self.temp_filepath):
            os.mkdir(self.temp_filepath)
        self.content = "bar\nbaz"
        self.filename = os.path.join(self.temp_filepath, "foo")
        with open(self.filename, "w") as f:
            f.write(self.content)

    def test_copy_file(self):
        # Arrange
        copy_filepath = os.path.join(self.temp_filepath, "copy")
        os.mkdir(copy_filepath)
        copy_filepath = os.path.join(copy_filepath, "copy_of_foo")

        # Act
        file_manager.copy_file(self.filename, copy_filepath)

        # Assert
        self.assertTrue(os.path.exists(copy_filepath))
        with open(copy_filepath, "r") as f:
            self.assertEqual(f.read(), self.content)

    def tearDown(self):
        shutil.rmtree(self.temp_filepath)
