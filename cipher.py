"""

    This module contains the functions to encrypt and decrypt a message using the
    well-known encryption algorithm called the caeser cipher.

    encrypt - takes a shift value and a file name and encrypts the file using the
                caeser cipher algorithm.

    decrypt - If a shift value is provided, the file is decrypted using that shift
                value. If no shift value is provided, the file is decrypted using
                all possible shift values, and the output is check against a 
                dictionary of words. The most likely shift value is then used to
                decrypt the file.

    Author: Jakob Lindo
    Created: 4/13/2023
    
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(shift, file):
    encr = ""

    with open(file, "r") as plaintext:
        for line in plaintext:
            for char in line:
                encr += alphabet[(alphabet.index(char) + shift) % 26]
    return encr


def decrypt(file, shift=-1):
    decr = ""

    with open(file, "r") as ciphertext:
        for line in ciphertext:
            for char in line:
                if shift == -1:
                    # Try all 26 shift values, comparing the decrypted string against
                    # a dictionary of words. The most hits is the most likely shift.
                    # Possibly break out early if every single word is a hit?
                    pass
                else:
                    decr += alphabet[(alphabet.index(char) - shift) % 26]
