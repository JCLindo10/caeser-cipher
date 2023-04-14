"""
This is a test file for the caeser-cipher module.
Author: Jakob Lindo
Created: 4/13/2023
"""
from ..src import main
import unittest
import sys
sys.path.append("..")


class TestCaeserCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(main.encrypt("e", 4, "test.txt"), "alex")
        self.assertEqual(main.encrypt("e", 30, "test2.txt"), "alex")
