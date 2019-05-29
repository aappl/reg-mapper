
import os

import cson

from context import reg_mapper
from reg_mapper import reg_map


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def test_get_reg_numbers():
    with open("../test/test.cson", 'r') as f:
        cson_data = f.read()
        maps = cson.loads(cson_data)

        reg_maps = reg_map.Map(maps)
        assert reg_maps.get_reg_numbers("my_register_map") == {
            'Temperature': 0,
            'Humidity': 1,
            'LEDs': 2,
            'Gyro1': 3,
            'Gyro2': 4
        }


def test_get_bits():
    with open("../test/test.cson", 'r') as f:
        cson_data = f.read()
        maps = cson.loads(cson_data)

        reg_maps = reg_map.Map(maps)

        print(reg_maps.get_bits("my_register_map", "LEDs"))

        assert reg_maps.get_bits("my_register_map", "LEDs") == {
            'Running': {
                'description': 'Shows that the device is running.',
                'start_bit': 0,
                'width': 1
            },
            'Error': {
                'description': 'Shows that there is an error in the device.',
                'start_bit': 1,
                'width': 1
            },
            'Count': {
                'description': 'The value of the internal counter.',
                'start_bit': 2,
                'width': 8
            }
        }
