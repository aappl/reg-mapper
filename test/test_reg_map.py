
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
        assert reg_maps.get_reg_addresses("my_register_map") == {
            'Temperature': 0,
            'Humidity': 4,
            'LEDs': 8,
            'Gyro1': 12,
            'Gyro2': 16
        }


def test_get_bits():
    with open("../test/test.cson", 'r') as f:
        cson_data = f.read()
        maps = cson.loads(cson_data)

        reg_maps = reg_map.Map(maps)

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


def test_set_addresses():
    with open("../test/test.cson", 'r') as f:
        cson_data = f.read()
        maps = cson.loads(cson_data)

        reg_maps = reg_map.Map(maps)

        reg_maps._set_addresses()

        assert reg_maps.maps["my_register_map"]["registers"]["Temperature"]["address"] == 0
        assert reg_maps.maps["my_register_map"]["registers"]["Humidity"]["address"] == 4
        assert reg_maps.maps["my_register_map"]["registers"]["LEDs"]["address"] == 8
        assert reg_maps.maps["my_register_map"]["registers"]["Gyro1"]["address"] == 12
        assert reg_maps.maps["my_register_map"]["registers"]["Gyro2"]["address"] == 16

        assert reg_maps.maps["my_register_map2"]["registers"]["Temperature"]["address"] == 0
        assert reg_maps.maps["my_register_map2"]["registers"]["Humidity"]["address"] == 4
        assert reg_maps.maps["my_register_map2"]["registers"]["LEDs"]["address"] == 8
        assert reg_maps.maps["my_register_map2"]["registers"]["Gyro1"]["address"] == 12
        assert reg_maps.maps["my_register_map2"]["registers"]["Gyro2"]["address"] == 16
