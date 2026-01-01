#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a JSON file.
"""
import sys

# Importing previously created functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# 1. Try to load existing data, or start empty if file is missing/broken
try:
    my_list = load_from_json_file(filename)
except (FileNotFoundError, ValueError):
    my_list = []

# 2. Get arguments from sys.argv (starting from index 1)
# sys.argv[0] is the script name, so we skip it
arguments = sys.argv[1:]

# 3. Add the arguments to our list and save
my_list.extend(arguments)
save_to_json_file(my_list, filename)
