"""

    Main entry point for the caeser-cipher program.
    Author: Jakob Lindo
    Created: 4/13/2023

"""

import sys
from optparse import OptionParser
from cipher import encrypt, decrypt


def main():
    """
    Main entry point for the caeser-cipher program.
    """

    # create an option parser, initialize
    parser = OptionParser()
    parser.add_option("-e", "--encrypt", action="store_true",
                      dest="encrypt", help="encrypt a file")
    parser.add_option("-d", "--decrypt", action="store_true",
                      dest="decrypt", help="decrypt a file")
    parser.add_option("-s", "--shift", action="store",
                      dest="shift", help="shift value")
    parser.add_option("-f", "--file", action="store",
                      dest="file", help="file to encrypt/decrypt")

    # parse the command line arguments
    (options, args) = parser.parse_args()

    if options.encrypt:
        if options.shift is None:
            print("Please provide a shift value. when encrypting a file.")
            sys.exit(1)
        if options.file is None:
            print("Please provide a file to encrypt.")
            sys.exit(1)
        encrypt(options.shift, options.file)

    if options.decrypt:
        if options.file is None:
            print("Please provide a file to decrypt.")
            sys.exit(1)
        if options.shift is None:
            decrypt(options.file)
        else:
            decrypt(options.file, options.shift)


if __name__ == "__main__":

    main()
