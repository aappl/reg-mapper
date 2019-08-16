"""
c_mapper
This module takes a generic map object and creates the C header file representing
a register map i.e. a set of definitions allowing the user to access a register
map using named addresses.
"""


def create_c(reg_map):
    """
    Create all C files necessary for a user to be able to access all registers
    in a register map.
    """
    c_text = create_header_file(reg_map)
    return c_text


def create_header_file(reg_map):
    """
    Create a header file text will definitions of all registers in map.
    """
    # Create variable to hold output C
    output_c = ""

    # Add registers and their addresses
    for reg_name, _ in reg_map.registers.items():
        reg = reg_map.registers[reg_name]
        output_c += "\n"
        output_c += c_define_value(reg.name + "_offset", reg.address_offset)
        for bit_group in reg.bit_groups:
            output_c += c_define_value(reg.name+"_"+bit_group.name+"_offset", bit_group.index)
            output_c += c_define_value(reg.name+"_"+bit_group.name+"_width", bit_group.width)
            output_c += c_define_value(reg.name+"_"+bit_group.name+"_mask", "0b"+("1"*bit_group.width)+" << "+str(bit_group.index))

    output_c += "\n"

    return output_c


def c_define_value(name, value):
    """
    Return a string with a definition of a constant value.
    """
    return "#define {} {}\n".format(name, value)
