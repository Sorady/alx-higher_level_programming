#!/usr/bin/python3
"""
Contains the function "write_file"
"""


def write_file(filename="", text=""):
    """Returns the number of characters written to a file from a given text.

    Args:
        filename (str): The name of the file to write. Defaults to "".
        text (str): The text to write to the file. Defaults to "".
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
