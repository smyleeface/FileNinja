import os
import shutil
import unittest
from unittest.mock import patch

import file_ninja.file_manager as file_manager


class CreateFileTest(unittest.TestCase):
    def setUp(self):
        self.temp_filepath = "/tmp/file_ninja_tests/"
        if not os.path.exists(self.temp_filepath):
            os.mkdir(self.temp_filepath)

    def test_create_without_content(self):
        # Arrange
        filename = os.path.join(self.temp_filepath, "foo")
        content = ""

        # Act
        file_manager.create(filename, content)

        # Assert
        self.assertTrue(os.path.exists(filename))
        with open(filename, "r") as f:
            self.assertEqual(f.read(), content)

    def test_create_with_content(self):
        # Arrange
        filename = os.path.join(self.temp_filepath, "foo")
        content = "bar\nbaz"

        # Act
        file_manager.create(filename, content)

        # Assert
        self.assertTrue(os.path.exists(filename))
        with open(filename, "r") as f:
            self.assertEqual(f.read(), content)

    @patch("file_ninja.app.file_manager.open", side_effect=Exception)
    def test_create_error(self, open_file_mock):
        # Arrange
        filename = os.path.join(self.temp_filepath, "foo")
        content = "bar\nbaz"

        # Act
        # Assert
        self.assertRaises(Exception, file_manager.create, filename, content)

    def tearDown(self):
        shutil.rmtree(self.temp_filepath)
