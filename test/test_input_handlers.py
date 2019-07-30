from pathlib import Path

from context import reg_mapper
from reg_mapper import reg_mapper
from reg_mapper.input_handlers import input_handlers


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
