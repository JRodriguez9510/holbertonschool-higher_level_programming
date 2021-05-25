#!/usr/bin/python3
"""
Module to print a name
"""


def say_my_name(first_name, last_name=""):
    """Prints the given name"""
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {:} {:}".format(first_name, last_name))
    else:
        raise TypeError('{:} must be a string'
                        .format('last_name' if isinstance(first_name, str)
                                else 'first_name'))
