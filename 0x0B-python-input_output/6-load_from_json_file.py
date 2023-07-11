#!/usr/bin/python3
"""6-load_from_json_file"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename (str): Name of JSON file.

    Returns:
        Deserialized object.
    """
    with open(filename, "r") as f:
        return json.load(f)
