
import pytest

from context import reg_mapper
from reg_mapper import reg_mapper
from reg_mapper import regs


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
                        'bits': {                               # bits is a keyword
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

    reg_maps = reg_mapper.RegMapper()
    reg_maps.add_map(test_map)

    assert reg_maps._maps[0].name == "map1"
