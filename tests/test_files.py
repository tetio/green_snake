# -*- coding: utf-8 -*-

from .context import green_snake

import unittest


class FilesTestSuite(unittest.TestCase):
    """File test cases."""

    def test_files_empty_folder(self):
        res = green_snake.getFilesFromFolder("no_files")
        self.assertTrue(not res, "It should be an empty folder!")

    def test_files_folder_with_one_file(self):
        res = green_snake.getFilesFromFolder("one_file")
        self.assertTrue(len(res) == 1, "It should be an empty folder!")

if __name__ == '__main__':
    unittest.main()
