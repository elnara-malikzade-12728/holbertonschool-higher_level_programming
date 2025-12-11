#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        part_1 = str[:n]
        part_2 = str[n+1:]
        new_str = part_1 + part_2
        return new_str
    else:
        return str
