#!/usr/bin/python3
"""
Module to print a square
"""


def print_square(size):
    """prints square of '#' of 'size' dimensions"""
    if isinstance(size, int):
        if size >= 0:
            for row in range(size):
                print('#' * size)
                row += 1
        else:
            raise ValueError('size must be >= 0')
    else:
        raise TypeError('size must be an integer')
