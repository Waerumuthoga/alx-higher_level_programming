#!/usr/bin/python3
"""Defines a rectangle subclass Square"""
Rectangle =__import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a  square"""

    def __init__(self, size):
        """Initializes a new square
        Arguments:
            size (int): The size of the new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
