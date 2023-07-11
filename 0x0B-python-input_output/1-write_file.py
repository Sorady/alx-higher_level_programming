#!/usr/bin/python3
"""1-write_file"""


def write_file(filename="", text=""):
    """
    Writes a string to a utf-8 text file.

    Args:
        filename (str): Filename. Defaults to an empty string.
        text (str): Text to write to file. Defaults to an empty string.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
