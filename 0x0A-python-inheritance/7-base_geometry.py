#!/usr/bin/python3
""" Module of a class BaseGeometry"""


class BaseGeometry():
    """ Class that defines geometry calculation """
    def __init__(self):
        """initializes new object of BaseGeometry Class"""
        pass

    def area(self):
        """defines area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if (value.__class__ != int):
            raise TypeError("{:} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{:} must be greater than 0".format(name))
