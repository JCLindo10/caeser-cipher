"""

    Main entry point for the caeser-cipher program.

    Author: Jakob Lindo

    Created: 4/13/2023

"""

import sys


def main():
    """
    Main entry point for the caeser-cipher program.

    """

    # option e = encrypt
    # using option e, the user must provide a shift value and a file to encrypt
    if sys.argv[1] == "e":
        shift = int(sys.argv[2])
        file = sys.argv[3]
        encrypt(shift, file)

    # option d = decrypt
    # using option d, the user must provide a file to decrypt. The user also has the option to provide a shift value.
    if sys.argv[1] == "d":
        if len(sys.argv) == 3:
            file = sys.argv[2]
            decrypt(file)
        else:
            shift = int(sys.argv[2])
            file = sys.argv[3]
            decrypt(file, shift)


if __name__ == "__main__":

    main()
