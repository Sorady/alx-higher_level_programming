#!/usr/bin/python3
"""This module contains a class Square that defines a square."""


class Square:
    """A class Square that defines a square."""
    def __init__(self, size=0):
        """Initializes the Square instance with a size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Retrieves the size of the Square instance."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the Square instance."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
