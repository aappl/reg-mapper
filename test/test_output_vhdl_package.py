"""
Test file for the output_vhdl_package module.
"""

from reg_mapper import output_vhdl_package
import test_utils


def test_create_vhdl():
    """
    Test that the created VHDL text is correct.
    """
    system = test_utils.create_test_object()

    output_vhdl = output_vhdl_package.create_vhdl_package(system.register_maps[0])

    print(output_vhdl)
    assert output_vhdl == """package test_map is

  constant test_register0 : integer := 0;
  constant test_register0_test_register0_bit_map0_0 : integer := 0;
  constant test_register0_test_register0_bit_map0_1 : integer := 1;
  constant test_register0_test_register0_bit_map0_2 : integer := 2;
  constant test_register0_test_register0_bit_map0_3 : integer := 3;
  constant test_register0_test_register0_bit_map1_0 : integer := 4;
  constant test_register0_test_register0_bit_map1_1 : integer := 5;
  constant test_register0_test_register0_bit_map1_2 : integer := 6;
  constant test_register0_test_register0_bit_map1_3 : integer := 7;

  constant test_register1 : integer := 1;
  constant test_register1_test_register1_bit_map0_0 : integer := 0;
  constant test_register1_test_register1_bit_map0_1 : integer := 1;
  constant test_register1_test_register1_bit_map0_2 : integer := 2;
  constant test_register1_test_register1_bit_map0_3 : integer := 3;
  constant test_register1_test_register1_bit_map1_0 : integer := 4;
  constant test_register1_test_register1_bit_map1_1 : integer := 5;
  constant test_register1_test_register1_bit_map1_2 : integer := 6;
  constant test_register1_test_register1_bit_map1_3 : integer := 7;

end package test_map;
"""
