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

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {:d}/{:d}".format(type(self).__name__, self.__width,
                                       self.__height)


class Square(Rectangle):
    """ Class inherited from Rectangle """
    def __init__(self, size):
        """ Initializes a new object Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Returns the area of a square """
        return self.__size ** 2

    def __str__(self):
        """ Returns string representation of the square """
        return "[{}] {}/{}".format(type(self).__name__, self.__size,
                                   self.__size)
