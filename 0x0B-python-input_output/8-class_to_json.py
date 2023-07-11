#!/usr/bin/python3
"""
Contains the function "class_to_json"
"""


def class_to_json(obj):
    """Returns the dictionary description of an object with a simple
        data structure.

    Args:
        obj: The object to convert to a dictionary.
    """
    return obj.__dict__
