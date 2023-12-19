#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A class that defines a square by its size
    """
    def __init__(self, size=0):
        """Method to initialize a square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method returns the area of the square
        """
        return (self.__size **2)
