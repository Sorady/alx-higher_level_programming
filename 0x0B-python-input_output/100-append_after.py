#!/usr/bin/python3
"""100-append_after"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.
    """
    lines = []
    with open(filename, "r") as f:
        for line in f:
            lines.append(line)
            if line.find(search_string) != -1:
                lines.append(new_string)

    with open(filename, "w") as f:
        f.writelines(lines)
