#!/usr/bin/python3
"""
Contains the function "from_json_string"
"""

import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to an object.
    """
    return json.loads(my_str)
