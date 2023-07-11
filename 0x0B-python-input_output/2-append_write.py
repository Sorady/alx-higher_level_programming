#!/usr/bin/python3
"""2-append_write"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a utf-8 text file.

    Args:
        filename (str): Filename. Defaults to an empty string.
        text (str): Text to append to file. Defaults to an empty string.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
