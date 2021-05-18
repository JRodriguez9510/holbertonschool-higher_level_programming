#!/usr/bin/python3
""" Square Module """


class Square:
    """ This is a square class """
    def __init__(self, size=0):
        """ Define size of the square """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """ Define are of the square """
        return self.__size**2

    @property
    def size(self):
        """ returns size variable of Square """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size variable of Square """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
