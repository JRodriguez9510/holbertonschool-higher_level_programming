#!/usr/bin/python3
""" module to confirm if the object is exactly an instance of a class """


def is_same_class(obj, a_class):
    """
    returns True if the object is exactly an instance of the specified class;
    otherwise False
    """
    return(obj.__class__ == a_class)
