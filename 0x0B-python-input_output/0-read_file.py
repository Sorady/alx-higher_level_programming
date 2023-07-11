#!/usr/bin/python3
"""0-read_file"""


def read_file(filename=""):
    """
    Reads a utf-8 text file and prints it to stdout.

    Args:
        filename (str): Name of the text file to read.
            Defaults to an empty string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
