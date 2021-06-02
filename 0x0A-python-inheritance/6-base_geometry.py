#!/usr/bin/python3
""" Module of a class BaseGeometry"""


class BaseGeometry():
    """ Initializes class """
    def __init__(self):
        """initializes new object of BaseGeometry Class"""
        pass
    """Class that defines geometry calculation """
    def area(self):
        """defines area """
        raise Exception("area() is not implemented")
