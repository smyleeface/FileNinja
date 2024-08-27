import os
import shutil
import unittest

import file_ninja.file_manager as file_manager


class MergeFileTest(unittest.TestCase):
    def setUp(self):
        self.temp_filepath = "/tmp/file_ninja_tests/"
        if not os.path.exists(self.temp_filepath):
            os.mkdir(self.temp_filepath)

        self.content = "bar\nbaz"
        self.filename = os.path.join(self.temp_filepath, "foo1")
        with open(self.filename, "w") as f:
            f.write(self.content)

        self.content2 = "bat\nqux"
        self.filename2 = os.path.join(self.temp_filepath, "foo2")
        with open(self.filename2, "w") as f:
            f.write(self.content2)

    def test_merge_files(self):
        # Arrange
        output_filepath = os.path.join(self.temp_filepath, "copy")
        os.mkdir(output_filepath)
        merged_filepath = os.path.join(output_filepath, "merged_files")

        # Act
        file_manager.merge_files(self.filename, self.filename2, merged_filepath)

        # Assert
        self.assertTrue(os.path.exists(merged_filepath))
        with open(merged_filepath, "r") as f:
            self.assertEqual(f.read(), "bar\nbazbat\nqux")

    def tearDown(self):
        shutil.rmtree(self.temp_filepath)
