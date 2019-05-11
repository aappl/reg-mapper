"""
vhdl_mapper
This module takes a generic map object and creates the VHDL text representing
a register map i.e. a set of constants allowing the user to access a register
map using named addresses.
"""


def create_vhdl(map):
    """
    Create a VHDL package with constants to allow the use of the register map.
    """
    # Create variable to hold the output VHDL
    output_vhdl = ""

    output_vhdl += vhdl_package_header(map)

    # Add registers and their addresses
    for reg in map.registers:
        output_vhdl += vhdl_register_address(reg)

    output_vhdl += vhdl_package_footer(map)

    return output_vhdl


def vhdl_package_header(map):
    """
    Return a string with the header for a VHDL package.
    """
    return "package {} is\n".format(map.name)


def vhdl_package_footer(map):
    """
    Return a string with the footer for a VHDL package.
    """
    return "end package {};\n".format(map.name)


def vhdl_register_address(reg):
    """
    Return a string with a VHDL constant declaration of the supplied
    register.
    """
    return "constant {} : integer := {};\n".format(reg.name, reg.address_offset)
