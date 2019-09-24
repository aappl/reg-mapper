"""
This is this top level user interface for the reg_mapper project.
"""


from pathlib import Path
import json

import cson

from reg_mapper import register_classes


class RegMapper():
    """
    The user interface to the Register Mapper library.
    """

    def __init__(self):
        self.system = register_classes.System()

    def add_map(self, map):
        """
        Fill the system attribute with register maps. This method converts the
        dictionary input into a Maps object.
        """
        register_maps = map['register_maps']
        for map_name, _ in register_maps.items():
            map = register_maps[map_name]  # map dictionary
            map_obj = register_classes.RegisterMap()  # map object

            # Fill in attributes of map object
            map_obj.name = map_name
            map_obj.width = map["width"]
            map_obj.base_address = map["base_address"]

            # Get registers in map
            registers = map['registers']
            for register_name, _ in registers.items():
                register = registers[register_name]  # register dictionary
                register_obj = register_classes.Register()  # register object

                # Fill in attributes of register object
                register_obj.name = register_name
                register_obj.rw = register["RW"]
                register_obj.description = register["description"]

                # Get bits in register
                bit_maps = register['bit_maps']
                for bit_name, _ in bit_maps.items():
                    bit = bit_maps[bit_name]  # bit dictionary
                    bit_obj = register_classes.BitMap()  # bit object

                    # Fill in attributes of bit object
                    bit_obj.name = bit_name
                    bit_obj.start_bit = bit["start_bit"]
                    bit_obj.width = bit["width"]
                    bit_obj.description = bit["description"]
                    bit_obj.generate_bits()

                    # Add bit to register object
                    register_obj.bit_maps.append(bit_obj)

                map_obj.registers.append(register_obj)

            map_obj.set_addresses()
            self.system.register_maps.append(map_obj)
