#!/usr/bin/python3
for c in range(97, 123):
  if chr(c)== 'q' or chr(c)=='o':
    continue
  print("{}".format(chr(c)), end="")
