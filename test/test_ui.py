
import pytest

from context import reg_mapper
from reg_mapper import ui
from reg_mapper import register_classes


def test_RegMapper_add_map():
    # Create a dictionary
    test_map = {
        'register_maps': {    # register_maps is a keyword
            'map1': {           # map1 will be used as the name of the register map
                "width": 32,    # width is a keyword
                "base_address": 0x0,  # base address is a keyword
                'registers': {    # registers is a keyword
                    'register1': {  # register1 will be used as the name of the register
                        'description': "The first register.",   # description is a keyword
                        'RW': 'READ_ONLY',                      # RW is a keyword
                        'bit_maps': {                             # bit_maps is a keyword
                            'bit1': {                             # bit1 will be used as the name of the bit
                                'description': "The first bit.",    # description is a keyword
                                'start_bit': 0,                     # start_bit is a keyword
                                'width': 3
                            }
                        }
                    }
                }
            }
        }
    }

    reg_maps = ui.RegMapper()
    reg_maps.add_map(test_map)

    # Test map
    assert reg_maps.system.register_maps[0].name == "map1"
    assert reg_maps.system.register_maps[0].width == 32
    assert reg_maps.system.register_maps[0].base_address == 0x0
    # Test register
    assert reg_maps.system.register_maps[0].registers[0].name == "register1"
    assert reg_maps.system.register_maps[0].registers[0].description == "The first register."
    assert reg_maps.system.register_maps[0].registers[0].rw == "READ_ONLY"
    # Test bit
    assert reg_maps.system.register_maps[0].registers[0].bit_maps[0].name == "bit1"
    assert reg_maps.system.register_maps[0].registers[0].bit_maps[0].description == "The first bit."
    assert reg_maps.system.register_maps[0].registers[0].bit_maps[0].start_bit == 0
    assert reg_maps.system.register_maps[0].registers[0].bit_maps[0].width == 3
