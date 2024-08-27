import os
import shutil
import unittest

import file_ninja.file_manager as file_manager


class DeleteFileTest(unittest.TestCase):
    def setUp(self):
        self.temp_filepath = "/tmp/file_ninja_tests/"
        if not os.path.exists(self.temp_filepath):
            os.mkdir(self.temp_filepath)

        self.content = "bar\nbaz"
        self.filename = os.path.join(self.temp_filepath, "foo")
        with open(self.filename, "w") as f:
            f.write(self.content)

    def test_delete_file(self):
        # Arrange
        # Act
        file_manager.delete_file(self.filename)

        # Assert
        self.assertFalse(os.path.exists(self.filename))

    def tearDown(self):
        shutil.rmtree(self.temp_filepath)
