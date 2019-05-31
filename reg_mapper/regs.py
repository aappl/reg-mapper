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


class BitGroup():
    """
    Class representing a group of bits in a register.
    """

    def __init__(self, name, index, width):
        self.name = name
        self.bits = []
        if width > 1:
            for index_num in range(index, index+width):
                bit_number = index_num - index
                self.bits.append(Bit(name + "_{}".format(bit_number), bit_number))
        else:
            self.bits.append(Bit(name, index))


class Register():
    """
    Class representing a register of bits.
    """

    def __init__(self, name, width, rw=None):
        self.name = name
        self._width = width
        self.bit_groups = []
        self.rw = rw
        self.address_offset = None
        self.description = ""


class Map():
    """
    Class representing a map of registers.
    """

    def __init__(self, name=None, width=32):
        self.name = name
        self._width = width
        # Check width is allowed
        if self._width not in VALID_WIDTHS:
            raise ValueError("Width value not allowed {}, valid values are {}".format(self._width, VALID_WIDTHS))
        self._address_count = 0
        self.registers = {}
        self.output_dir = Path("register_maps")
        self.base_address = None

    def add_register(self, name, rw):
        """
        Create and add a new register to the map.
        """
        if rw not in VALID_WRITE_PROTECTION:
            raise ValueError("{} is not a valid input, valid inputs are {}".format(rw, VALID_WRITE_PROTECTION))

        self.registers[name] = Register(name, self._width)

    def add_bit_map(self, reg_name, bit_number, width, bit_name):
        """
        Set the name of a bit or group of bits in the register.
        """
        self.registers[reg_name].bit_groups.append(BitGroup(bit_name, bit_number, width))

    @property
    def output_dir(self):
        """
        Returns without modification.
        """
        return self.__output_dir

    @output_dir.setter
    def output_dir(self, output_dir):
        """
        Setter for output directory ensures the input gets converted to a Path
        type before being stored.
        """
        self.__output_dir = Path(output_dir)

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

    def add_register_description(self, reg_name, description):
        """
        Add a description to a register.
        """
        self.registers[reg_name].description = description

    def create(self, output_types):
        """
        Create the output register map files
        """
        # Check that the imput list values are all valid
        if set(output_types).issubset(VALID_OUTPUT_TYPES):
            # For every requested output type, create the output file
            for output_type in output_types:
                if output_type == "vhdl":
                    vhdl_mapper.create_vhdl(self)
                if output_type == "verilog":
                    raise NotImplementedError()
                if output_type == "c":
                    raise NotImplementedError()
                if output_type == "html":
                    raise NotImplementedError()
        else:
            raise ValueError("Input for output file types is invalid")
