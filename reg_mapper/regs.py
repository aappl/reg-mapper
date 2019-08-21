"""
regs
The regs module contains classes describing the elements of a register map.
For example, a register class defining a name and address offset, or a bit
class representing a single bit in a register with a name.
"""

from reg_mapper import exceptions


VALID_WRITE_PROTECTION = ["READ_WRITE", "READ_ONLY", "WRITE_ONLY"]
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


class BitMap():
    """
    Class representing a group of bits in a register.
    """

    def __init__(self):
        self.name = None
        self.bits = []
        self.start_bit = None
        self.width = None
        self.description = None

    def generate_bits(self):
        if self.width > 1:
            for index_num in range(self.start_bit, self.start_bit+self.width):
                bit_number = index_num - self.start_bit
                self.bits.append(Bit(self.name + "_{}".format(bit_number), index_num))
        else:
            self.bits.append(Bit(self.name, self.start_bit))


class Register():
    """
    Class representing a register of bits.
    """

    def __init__(self):
        self.name = None
        self.rw = "READ_ONLY"  # TODO add protection to make sure only the values above can be set
        self.description = ""
        self.bit_maps = []
        self.address_offset = None

    def check_bit_maps(self):
        """
        Check that the bit maps don't overlap.
        """
        bits_in_use = []
        for bit_map in self.bit_maps:
            for bit in bit_map.bits:
                if bit.number in bits_in_use:
                    raise exceptions.BitAssignmentError("\n\nBit assigned multiple times\nRegister : {}\nBit: {}\n".format(self.name, bit.number))
                else:
                    bits_in_use.append(bit.number)


class Map():
    """
    Class representing a map of registers.
    """

    def __init__(self):
        self.name = None
        self.width = None  # TODO add protection to make sure only the values above can be set
        self.registers = []
        self.base_address = None

    def set_addresses(self):
        """
        Set the addresses of the registers in the map.
        """
        word_size_bytes = self.width / 8
        address = 0
        for reg in self.registers:
            reg.address_offset = int(address)
            address += word_size_bytes
