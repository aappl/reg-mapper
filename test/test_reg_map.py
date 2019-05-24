
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
        assert reg_maps.get_reg_numbers() == {
            'my_register_map': {
                'Temperature': 0,
                'Humidity': 1,
                'LEDs': 2,
                'Gyro1': 3,
                'Gyro2': 4
            },
            'my_register_map2': {
                'Temperature': 0,
                'Humidity': 1,
                'LEDs': 2,
                'Gyro1': 3,
                'Gyro2': 4
            }
        }
