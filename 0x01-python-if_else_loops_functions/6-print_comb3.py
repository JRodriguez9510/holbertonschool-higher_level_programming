#!/usr/bin/python3
for i in range(1, 90):
    if i < 10:
        print("{:02d}, ".format(i), end="")
    if i > 9 and i < 89 and i / 10 != i % 10 and i / 10 < i % 10:
        print("{}, ".format(i), end="")
    if i == 89:
        print("{}".format(i))
