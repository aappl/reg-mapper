
from context import reg_mapper
from reg_mapper import register_classes


def create_test_object():
    # Create system
    system = register_classes.System()

    # Create register map object
    register_map = register_classes.RegisterMap()
    register_map.name = "test_map"
    register_map.width = 8
    register_map.base_address = 0

    # Create test registers
    for reg_count in range(2):
        register = register_classes.Register()
        register.name = "test_register" + str(reg_count)
        register.rw = "RW"

        # Add bit maps to the registers
        bit_map0 = register_classes.BitMap()
        bit_map0.name = register.name + "_bit_map0"
        bit_map0.start_bit = 0
        bit_map0.width = 4
        bit_map0.generate_bits()

        bit_map1 = register_classes.BitMap()
        bit_map1.name = register.name + "_bit_map1"
        bit_map1.start_bit = 4
        bit_map1.width = 4
        bit_map1.generate_bits()

        register.bit_maps.append(bit_map0)
        register.bit_maps.append(bit_map1)

        register_map.registers.append(register)


    register_map.set_addresses()

    system.register_maps.append(register_map)

    return system


if __name__ == '__main__':
    create_test_object()
