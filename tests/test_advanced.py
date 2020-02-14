# -*- coding: utf-8 -*-

from .context import green_snake

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(green_snake.hmm())


if __name__ == '__main__':
    unittest.main()
