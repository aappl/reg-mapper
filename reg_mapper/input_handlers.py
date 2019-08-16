"""
This file contains functions that convert input files into dictionaries. The dictionaries can then
be passed to the RegMapper class.
"""

from pathlib import Path
import json


import cson

input_handlers = []


def json_handler(file_path):
    """
    Handles json file inputs. Takes Path object pointing to json file and returns
    a python dictionary with the json files contents
    """
    if file_path.suffix == '.json':
        with open(file_path, "r") as read_file:
            data = json.load(read_file)
            return data


input_handlers.append(json_handler)


def cson_handler(file_path):
    """
    Handles cson file inputs. Takes Path object pointing to cson file and returns
    a python dictionary with the cson files contents
    """
    if file_path.suffix == '.cson':
        with open(file_path, "r") as read_file:
            data = cson.load(read_file)
            return data

    else:
        return None


input_handlers.append(cson_handler)


def get_dicts(input_files):
    """
    Takes a list of input path strings and returns the dictionary contents.
    """
    input_dicts = []
    for f in input_files:
        for handler in input_handlers:
            input_dict = handler(Path(f))
            if input_dict:
                input_dicts.append(input_dict)

    return input_dicts
