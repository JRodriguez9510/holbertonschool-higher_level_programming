#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        j = ord(str[i])
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            j -= 32
        print("{}".format(chr(j)), end="")
    print()
