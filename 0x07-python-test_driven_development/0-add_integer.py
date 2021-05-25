#!/usr/bin/python3
"""
Module to add to integers
"""


def add_integer(a, b=98):
    """function to add a and b"""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return int(a) + int(b)
    else:
        raise TypeError("{:} must be an integer"
                        .format('b' if isinstance(a, (int, float)) else 'a'))
