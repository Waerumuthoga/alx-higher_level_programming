#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Class Square that defines a square by its size."""

    def __init__(self, size=0):
        """Method responsible for initializing square of object"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
