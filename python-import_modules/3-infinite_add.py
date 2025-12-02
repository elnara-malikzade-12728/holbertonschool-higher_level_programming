#!/usr/bin/python3
from calculator_1 import add
import sys
if __name__ == "__main__":
    argv = sys.argv[0:]
    count = len(argv)
    for i in range(count):
        print("{} ".format(int(add(i, i))))
