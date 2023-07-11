#!/usr/bin/python3
"""4-from_json_string"""
import json


def from_json_string(my_str):
    """
    Deserializes a JSON string into a python object.

    Args:
        my_str (str): JSON string

    Returns:
        An object represented by the JSON string.
    """
    return json.loads(my_str)
