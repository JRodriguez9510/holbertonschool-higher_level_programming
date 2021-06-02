#!/usr/bin/python3
""" Module of a inherited class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class inherited form BaseGeometry """
    def __init__(self, width, height):
        """ Initializes a new object Rectangle """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
