from pathlib import Path

from ruamel.yaml import YAML

from context import reg_mapper
from reg_mapper.input_handlers import yaml_handler
from reg_mapper.input_handlers import get_dicts


def test_input_handlers():

    test_file = Path("test/test1.yaml")

    test_dict = yaml_handler(test_file)

    yaml = YAML()
    with open(test_file, 'r') as f:
        actual_dict = yaml.load(f)

    assert test_dict == actual_dict


def test_get_dicts():

    test_files = ["test/test1.yaml", "test/test2.yaml"]
    dicts = get_dicts(test_files)

    actual_dicts = []
    yaml = YAML()
    with open(test_files[0], 'r') as f:
        actual_dicts.append(yaml.load(f))
    with open(test_files[1], 'r') as f:
        actual_dicts.append(yaml.load(f))

    assert dicts == actual_dicts
