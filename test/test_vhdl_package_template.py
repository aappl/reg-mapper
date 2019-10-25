from mako.template import Template

from context import reg_mapper
from reg_mapper import register_classes


def test_vhdl_package_template():
    vhdl_template = Template(filename="reg_mapper/templates/vhdl_package.vhd")

    register_map = register_classes.RegisterMap()
    register_map.name = "test_package"
    register_map.width = 32

    for reg in range(10):
        register = register_classes.Register()
        register.name = "register_" + str(reg)
        for bit in range(2):
            bit_map = register_classes.BitMap()
            bit_map.name = "bit_map" + str(bit)
            bit_map.start_bit = bit
            register.bit_maps.append(bit_map)
        register_map.registers.append(register)

    register_map.set_addresses()

    expected = """
library IEEE;
use IEEE.std_logic_1164.all;

package test_package is

  -- Registers
  constant register_0 : integer := 0;
  constant register_1 : integer := 4;
  constant register_2 : integer := 8;
  constant register_3 : integer := 12;
  constant register_4 : integer := 16;
  constant register_5 : integer := 20;
  constant register_6 : integer := 24;
  constant register_7 : integer := 28;
  constant register_8 : integer := 32;
  constant register_9 : integer := 36;

  -- Bit maps
  -- register_0 bit map
  constant register_0_bit_map0 : integer := 0
  constant register_0_bit_map1 : integer := 1

  -- register_1 bit map
  constant register_1_bit_map0 : integer := 0
  constant register_1_bit_map1 : integer := 1

  -- register_2 bit map
  constant register_2_bit_map0 : integer := 0
  constant register_2_bit_map1 : integer := 1

  -- register_3 bit map
  constant register_3_bit_map0 : integer := 0
  constant register_3_bit_map1 : integer := 1

  -- register_4 bit map
  constant register_4_bit_map0 : integer := 0
  constant register_4_bit_map1 : integer := 1

  -- register_5 bit map
  constant register_5_bit_map0 : integer := 0
  constant register_5_bit_map1 : integer := 1

  -- register_6 bit map
  constant register_6_bit_map0 : integer := 0
  constant register_6_bit_map1 : integer := 1

  -- register_7 bit map
  constant register_7_bit_map0 : integer := 0
  constant register_7_bit_map1 : integer := 1

  -- register_8 bit map
  constant register_8_bit_map0 : integer := 0
  constant register_8_bit_map1 : integer := 1

  -- register_9 bit map
  constant register_9_bit_map0 : integer := 0
  constant register_9_bit_map1 : integer := 1

end package;
"""

    assert vhdl_template.render(map_name=register_map.name, register_map=register_map) == expected.replace('\n', '\r\n')
