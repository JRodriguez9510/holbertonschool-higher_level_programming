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
