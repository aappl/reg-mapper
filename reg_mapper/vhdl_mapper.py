"""
vhdl_mapper
This module takes a generic map object and creates the VHDL text representing
a register map i.e. a set of constants allowing the user to access a register
map using named addresses.
"""


def create_vhdl(reg_map):
    """
    Create a VHDL package with constants to allow the use of the register map.
    """
    # Create variable to hold the output VHDL
    output_vhdl = ""

    output_vhdl += vhdl_package_header(reg_map.name)

    # Add registers and their addresses
    registers_vhdl = ""
    bits_vhdl = ""
    for reg_name, _ in reg_map.registers.items():
        reg = reg_map.registers[reg_name]
        registers_vhdl += vhdl_register_address(reg.name, reg.address_offset)
        for bit_group in reg.bit_groups:
            for bit in bit_group.bits:
                bits_vhdl += vhdl_bit_name(bit.name, bit.number)

    output_vhdl += registers_vhdl
    output_vhdl += bits_vhdl

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


def vhdl_bit_name(name, number):
    """
    Returns a string with a VHDL constant delaration of a bit name and it's
    associted number.
    """
    return "constant {} : integer := {};\n".format(name, number)
