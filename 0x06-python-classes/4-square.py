#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """A class that defines a square by its size
    """
    def __init__(self, size=0):
        """Method to initialize the square object
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method that return the area of a square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Method that return the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Method that sets the value of size of the square object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
