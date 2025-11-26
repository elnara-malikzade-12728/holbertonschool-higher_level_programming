#!/usr/bin/python3
for i in range(0, 100):
    ones = i % 10
    tens = (i // 10) % 10
    if ones <= tens:
        continue
    if i != 89:
        print("{:02}, ".format(i), end='')
    else:
        print("{:02}".format(i))
