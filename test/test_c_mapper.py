
from context import reg_mapper
from reg_mapper import reg_mapper
from reg_mapper import c_mapper


def test_create_c():
    # Create a new map object with a name and a size
    register_map = reg_mapper.RegMapper("test.cson")

    output_c = c_mapper.create_c(register_map.map_objs["my_register_map"])

    print(output_c)
    assert output_c == """\

#define Temperature_offset 0

#define Humidity_offset 4

#define LEDs_offset 8
#define LEDs_Running_offset 0
#define LEDs_Running_width 1
#define LEDs_Running_mask 0b1 << 0
#define LEDs_Error_offset 1
#define LEDs_Error_width 1
#define LEDs_Error_mask 0b1 << 1
#define LEDs_Count_offset 2
#define LEDs_Count_width 8
#define LEDs_Count_mask 0b11111111 << 2

#define Gyro1_offset 12

#define Gyro2_offset 16

"""
