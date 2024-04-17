#!/usr/bin/python3
"""
module only sub class of
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
    that onherited (directly or indirectly) from the specified class;
    otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
