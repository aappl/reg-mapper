"""
test_vhdl_mapper
Test file for the vhdl_mapper module.
"""

from pathlib import Path

from context import reg_mapper
from reg_mapper import reg_mapper
from reg_mapper import regs
from reg_mapper import vhdl_mapper


def test_create_vhdl(tmpdir):
    """
    Test that the created VHDL text is correct.
    """
    # Create a new map object with a name and a size
    register_map = reg_mapper.RegMapper("test.cson")

    output_vhdl = vhdl_mapper.create_vhdl(register_map.map_objs["my_register_map"])

    assert output_vhdl == """\
package my_register_map is
constant Temperature : integer := 0;
constant Humidity : integer := 4;
constant LEDs : integer := 8;
constant Gyro1 : integer := 12;
constant Gyro2 : integer := 16;
constant Running : integer := 0;
constant Error : integer := 1;
constant Count_0 : integer := 0;
constant Count_1 : integer := 1;
constant Count_2 : integer := 2;
constant Count_3 : integer := 3;
constant Count_4 : integer := 4;
constant Count_5 : integer := 5;
constant Count_6 : integer := 6;
constant Count_7 : integer := 7;
end package my_register_map;
"""
