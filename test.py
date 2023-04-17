"""

    This is a test file for the caeser-cipher module.
    Author: Jakob Lindo
    Created: 4/13/2023

"""
from src import main
import unittest
import sys
sys.path.append("..")


class TestCaeserCipher(unittest.TestCase):
    def test_encrypt_equal(self):
        self.assertEqual(main.encrypt("e", 4, "test.txt"), "alex")
        self.assertEqual(main.encrypt("e", 30, "test.txt"), "alex")

    def test_encrypt_not_equal(self):
        self.assertNotEqual(main.encrypt("e", 7, "test.txt"), "alex")
        self.assertNotEqual(main.encrypt("e", 3, "test.txt"), "alex")

    def test_decrypt_equal(self):
        self.assertEqual(main.decrypt("test.txt", 4), "what")
        self.assertEqual(main.decrypt("test.txt", 30), "what")
        self.assertEqual(main.decrypt("test.txt"), "what")

    def test_decrypt_not_equal(self):
        self.assertNotEqual(main.decrypt("test.txt", 7), "what")
        self.assertNotEqual(main.decrypt("test.txt", 3), "what")
        self.assertNotEqual(main.decrypt("test.txt"), "tahw")


if __name__ == "__main__":
    unittest.main()
