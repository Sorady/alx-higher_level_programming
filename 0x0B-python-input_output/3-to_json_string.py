#!/usr/bin/python3
"""
Contains the function "to_json_string"
"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj: The object to convert to JSON.
    """
    return json.dumps(my_obj)
