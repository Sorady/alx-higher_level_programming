#!/usr/bin/python3
"""8-class_to_json"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj (Any): The object.

    Returns:
        Dictionary.
    """
    if "__dict__" in dir(obj):
        return obj.__dict__.copy()
    return {}
