#!/usr/bin/python3
"""9-student"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student with name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a json representation of a Student instance"""
        return self.__dict__.copy()
