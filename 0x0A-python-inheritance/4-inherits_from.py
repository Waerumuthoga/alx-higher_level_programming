#!/usr/bin/python3
"""Defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.
    Arguments:
        obj (any): the object to be checked
        a_class (type): the class to match the type of object to
    Returns:
        If object is an inherited instance of a_class - True
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
