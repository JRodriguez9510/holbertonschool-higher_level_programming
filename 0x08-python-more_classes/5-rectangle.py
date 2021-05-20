#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle:
    """This is a Rectangle class"""
    def __init__(self, width=0, height=0):
        """Inilization of the width and height of the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns width variable of Square class instance """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value for Rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height variable of Square class instance """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets heigth value for Rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            p = 0
        else:
            p = self.__width * 2 + self.__height * 2
        return p

    def __str__(self):
        """Prints the rectangle made with # signs"""
        st = ''
        if self.__width == 0 or self.__height == 0:
            return st
        else:
            for h in range(self.__height):
                st += str('#' * self.__width + '\n')
                h += 1
        return st[:-1]

    def __repr__(self):
        """returns representation of a rectangle"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """deletes a rectangle"""
        return print("Bye rectangle...")
