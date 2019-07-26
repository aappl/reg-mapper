"""
regs
The regs module contains classes describing the elements of a register map.
For example, a register class defining a name and address offset, or a bit
class representing a single bit in a register with a name.
"""

from pathlib import Path

from reg_mapper import vhdl_mapper
from reg_mapper import exceptions


VALID_WRITE_PROTECTION = ["READ_WRITE", "READ_ONLY"]
VALID_OUTPUT_TYPES = ["vhdl", "verilog", "c", "html"]
VALID_WIDTHS = [8, 16, 32, 64, 128, 256, 512, 1024]


class Bit():
    """
    Class representing one bit in a register.
    """

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return "{} : {}".format(self.number, self.name)


class Bits():
    """
    Class representing a group of bits in a register.
    """

    def __init__(self):
        self.name = None
        self._bits = []
        self.start_bit = None
        self.width = None

    def generate_bits(self):
        if self.width > 1:
            for index_num in range(self.start_bit, self.start_bit+self.width):
                bit_number = index_num - self.start_bit
                self._bits.append(Bit(self.name + "_{}".format(bit_number), bit_number))
        else:
            self._bits.append(Bit(self.name, self.start_bit))


class Register():
    """
    Class representing a register of bits.
    """

    def __init__(self):
        self.name = None
        self.rw = "READ_ONLY"
        self.description = ""
        self.bits = []
        self._address_offset = None


class Map():
    """
    Class representing a map of registers.
    """

    def __init__(self):
        self.name = None
        self.width = None
        self.registers = []
        self.base_address = None

    def set_addresses(self):
        """
        Set the addresses of the registers in the map.
        """
        word_size_bytes = self._width / 8
        address = 0
        for _, reg in self.registers.items():
            reg.address_offset = int(address)
            address += word_size_bytes

    def _check_bit_groups(self):
        """
        Check that the bit groups don't overlap.
        """
        bits_in_use = []
        for _, reg in self.registers.items():
            for group in reg.bit_groups:
                for bit in group.bits:
                    if bit.number in bits_in_use:
                        raise exceptions.BitAssignmentError("\n\nBit assigned multiple times\nRegister : {}\nBit: {}\n".format(reg.name, bit.number))
                    else:
                        bits_in_use.append(bit.number)
