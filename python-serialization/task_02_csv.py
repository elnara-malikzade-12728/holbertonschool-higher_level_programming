#!/usr/bin/env python3
"""Defines a function that takes the CSV filename
 as its parameter and writes the JSON data to data.json."""
import csv
import json

def convert_csv_to_json(csv_file):
    """Converts a CSV file to JSON."""
    try:
        dict_reader = csv.DictReader(csv_file)
        with open(csv_file, mode='r', encoding='utf-8') as f:
            dict_reader = csv.DictReader(f)
            data = list(dict_reader)

        with open('data.json', 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            return True
    except FileNotFoundError:
        return False


