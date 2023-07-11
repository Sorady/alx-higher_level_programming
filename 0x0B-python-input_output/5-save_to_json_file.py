#!/usr/bin/python3
"""5-save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (Any): The object to write.
        filename (str): Name of file to write to.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
