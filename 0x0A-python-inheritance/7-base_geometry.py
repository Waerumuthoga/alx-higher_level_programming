#!/usr/bin/pyhton3
"""Defines a base geometry class BaseGeometry."""

class BaseGeometry:
    """Represents base geometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameteer as an integer.
        Arguments:
            name (str): The name of the parameter
            value (int): The parameter to validate
        Raises:
            TypeError: If value is not an integer
            ValueError: if valuse is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
