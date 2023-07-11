#!/usr/bin/python3
"""This module contains a class Rectangle that defines a rectangle."""


class Rectangle:
    """A class Rectangle that defines a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the Rectangle instance with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle instance."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the height of the Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle instance."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the Rectangle instance."""
        return 2 * (self.width + self.height) \
            if self.width != 0 and self.height != 0 else 0

    def __str__(self):
        """Returns a string representation of the Rectangle instance."""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(
                [str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """Returns a string representation of the Rectangle instance."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
