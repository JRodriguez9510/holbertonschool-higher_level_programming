#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    t = (tuple_a, tuple_b)
    for i in range(2):
        if len(t[0]) > i:
            a[i] += t[0][i]
        if len(t[1]) > i:
            a[i] += t[1][i]
    return (a[0], a[1])
