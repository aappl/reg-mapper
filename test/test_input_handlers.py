from pathlib import Path

from context import reg_mapper
from reg_mapper.input_handlers import input_handlers
from reg_mapper.input_handlers import get_dicts


def test_input_handlers():
    import json

    test_file = Path("test/test.json")

    test_dicts = []
    for handler in input_handlers:
        test_dicts.append(handler(test_file))

    with open(test_file, 'r') as f:
        actual_dict = json.load(f)

    assert test_dicts[0] == actual_dict
    assert test_dicts[1] is None


def test_get_dicts():
    import json
    import cson

    test_files = ["test/test.json", "test/test.cson"]
    dicts = get_dicts(test_files)
    print(dicts)

    actual_dicts = []
    with open(test_files[0], 'r') as f:
        actual_dicts.append(json.load(f))
    with open(test_files[1], 'r') as f:
        actual_dicts.append(cson.load(f))

    assert dicts == actual_dicts
