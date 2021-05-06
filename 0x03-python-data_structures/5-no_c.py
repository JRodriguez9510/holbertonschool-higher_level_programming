#!/usr/bin/python3
def no_c(my_string):
    c_nt = ''
    for i in my_string:
        if i not in 'Cc':
            c_nt = c_nt + i
    return c_nt
