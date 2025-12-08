#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_items = sorted(a_dictionary.items())
    sorted_dict_by_key = dict(sorted_items)
    return sorted_dict_by_key
