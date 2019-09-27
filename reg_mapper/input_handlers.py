"""
This file contains functions that convert input files into dictionaries. The dictionaries can then
be passed to the RegMapper class.
"""

from pathlib import Path

from ruamel.yaml import YAML


YAML_EXTS = [".yaml", ".yml"]


def yaml_handler(file_path):
    """
    Handles YAML file inputs. Takes Path object pointing to YAML file and returns
    a python dictionary with the YAML files contents
    """
    if file_path.suffix in YAML_EXTS:
        with file_path.open("r") as read_file:
            yaml = YAML()
            data = yaml.load(read_file)
            return data
    else:
        raise Exception("File extension not recognised: " + file_path.suffix)


def get_dicts(input_files):
    """
    Takes a list of input path strings and returns the dictionary contents.
    """
    input_dicts = []
    for f in input_files:
        input_dict = yaml_handler(Path(f))
        if input_dict:
            input_dicts.append(input_dict)

    return input_dicts
