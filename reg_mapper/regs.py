"""
regs
The regs module contains classes describing the elements of a register map.
For example, a register class defining a name and address offset, or a bit
class representing a single bit in a register with a name.
"""

from pathlib import Path

from reg_mapper import vhdl_mapper


VALID_WRITE_PROTECTION = ["READ_WRITE", "READ_ONLY"]
VALID_OUTPUT_TYPES = ["vhdl", "verilog", "c", "html"]


class Bit():
    """
    Class representing one bit in a register.
    """

    def __init__(self, number):
        self.name = None
        self.number = number


class Register():
    """
    Class representing a register of bits.
    """

    def __init__(self, name=None, width=None, rw=None, address_offset=None):
        self.name = name
        self.width = width
        if width:
            # Create empty set of bits
            self.bits = [Bit(i) for i in range(width)]
        else:
            self.bits = None

        self.rw = rw
        self.address_offset = address_offset


class Map():
    """
    Class representing a map of registers.
    """

    def __init__(self, name=None, width=32):
        self.name = name
        self._width = width
        self._address_count = 0
        self.registers = {}
        self.output_dir = Path("register_maps")
        self.base_address = None

    def add_register(self, name, rw):
        """
        Create and add a new register to the map.
        """
        if rw in VALID_WRITE_PROTECTION:
            self.registers[name] = Register(
                                        name,
                                        width=self._width,
                                        address_offset=self._address_count)
            self._address_count += 1
        else:
            raise ValueError("{} is not a valid input, valid inputs \
                              are {}".format(rw, VALID_WRITE_PROTECTION))

    def set_bit_name(self, reg_name, bit_number, bit_name):
        self.registers[reg_name].bits[bit_number].name = bit_name

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
