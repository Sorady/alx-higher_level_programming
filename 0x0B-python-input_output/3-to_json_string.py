#!/usr/bin/python3
"""3-to_json_string"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object.

    Args:
        my_obj (Any): Object to be serialized.

    Returns:
        The JSON representation of an object.
    """
    return json.dumps(my_obj)
