
def create(map):
    for reg in map.registers:
        print(vhdl_package_header(map))
        print("Register name, address: {}, {}".format(reg.name, reg.address_offset))
        print(vhdl_register_address(reg))


def vhdl_package_header(map):
    return "package {} is".format(map.name)

def vhdl_register_address(reg):
    """
    Return a string with a VHDL constant declaration of the supplied
    register.
    """
    return "constant {} : integer := {};".format(reg.name, reg.address_offset)
