"""

    This is a test file for the caeser-cipher module.
    Author: Jakob Lindo
    Created: 4/13/2023

"""
import cipher as Cipher
import unittest
# import sys
# sys.path.append("..")

# Test1sol.txt expects a shift of 7


class TestCaeserCipher(unittest.TestCase):
    def test_encrypt_equal(self):
        self.assertEqual(Cipher.encrypt(4, "test.txt"), "alex")
        self.assertEqual(Cipher.encrypt(30, "test.txt"), "alex")

    def test_encrypt_not_equal(self):
        self.assertNotEqual(Cipher.encrypt(7, "test.txt"), "alex")
        self.assertNotEqual(Cipher.encrypt(3, "test.txt"), "alex")

    def test_decrypt_equal(self):
        self.assertEqual(Cipher.decrypt("test.txt", 4), "what")
        self.assertEqual(Cipher.decrypt("test.txt", 30), "what")
        self.assertEqual(Cipher.decrypt("test.txt"), "what")

    def test_decrypt_not_equal(self):
        self.assertNotEqual(Cipher.decrypt("test.txt", 7), "what")
        self.assertNotEqual(Cipher.decrypt("test.txt", 3), "what")
        self.assertNotEqual(Cipher.decrypt("test.txt"), "tahw")


if __name__ == "__main__":
    unittest.main()
