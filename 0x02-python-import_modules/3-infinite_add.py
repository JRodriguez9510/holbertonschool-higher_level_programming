#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys.argv)
    total = 0

    for i in range(1, n):
        total += int(sys.argv[i])
    print(total)
