"""
This file contains functions that convert input files into dictionaries. The dictionaries can then
be passed to the RegMapper class.
"""

import json
import cson

input_handlers = []


def json_handler(file_path):
    if file_path.suffix == '.json':
        print("In json")
        with open(file_path, "r") as read_file:
            data = json.load(read_file)
            return data


input_handlers.append(json_handler)


def cson_handler(file_path):
    if file_path.suffix == '.cson':
        print("In cson")
        with open(file_path, "r") as read_file:
            data = cson.load(read_file)
            return data

    else:
        return None


input_handlers.append(cson_handler)
