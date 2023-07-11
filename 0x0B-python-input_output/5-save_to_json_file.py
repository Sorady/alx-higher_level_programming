#!/usr/bin/python3
"""Module for save_to_json_file method"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, us
    ing a JSON representation"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
