"""
This module takes a generic map object and creates the VHDL text representing
a register map i.e. a set of constants allowing the user to access a register
map using named addresses.
"""


INDENT = "  "


def create_vhdl_package(reg_map):
    """
    Create a VHDL package with constants to allow the use of the register map.
    """
    # Create variable to hold the output VHDL
    output_vhdl = ""

    output_vhdl += vhdl_package_header(reg_map.name)

    # Add registers and their addresses
    for reg in reg_map.registers:
        output_vhdl += "\n"
        output_vhdl += INDENT + vhdl_register_address(reg.name, reg.address_offset)
        for bit_map in reg.bit_maps:
            for bit in bit_map.bits:
                output_vhdl += INDENT + vhdl_bit_name(reg.name, bit.name, bit.number)

    output_vhdl += "\n"

    output_vhdl += vhdl_package_footer(reg_map.name)

    return output_vhdl


def vhdl_package_header(name):
    """
    Return a string with the header for a VHDL package.
    """
    return "package {} is\n".format(name)


def vhdl_package_footer(name):
    """
    Return a string with the footer for a VHDL package.
    """
    return "end package {};\n".format(name)


def vhdl_register_address(name, address_offset):
    """
    Return a string with a VHDL constant declaration of the supplied
    register.
    """
    return "constant {} : integer := {};\n".format(name, address_offset)


def vhdl_bit_name(reg_name, bit_name, number):
    """
    Returns a string with a VHDL constant delaration of a bit name and it's
    associted number.
    """
    return "constant {}_{} : integer := {};\n".format(reg_name, bit_name, number)
