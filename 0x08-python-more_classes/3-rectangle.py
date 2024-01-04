#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represents a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a  new Rectangle.
        width: is the new width of the new rectangle
        height: is the new height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the new Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance (value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the new Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance (value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle,
        representing it with #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for j in range(self.__height):
            [rect.append('#') for i in range(self.__width)]
            if j != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
