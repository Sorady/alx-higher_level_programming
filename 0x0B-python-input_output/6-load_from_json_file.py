#!/usr/bin/python3
"""
Contains the function "load_from_json_file"
"""

import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
