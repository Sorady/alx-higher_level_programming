#!/usr/bin/python3
"""check if object if instance of a class that
inherited from specified class"""


def inherits_from(obj, a_class):
    """return True if object is an instance of a class that
    inherited from specified class"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
