"""
test_vhdl_mapper
Test file for the vhdl_mapper module.
"""

from pathlib import Path

from context import reg_mapper
from reg_mapper import regs
from reg_mapper import vhdl_mapper


def test_create_vhdl(tmpdir):
    """
    Test that the created VHDL text is correct.
    """
    # Create a new map object with a name and a size
    register_map = regs.Map("system", 32)

    # Create the map by adding registers
    register_map.add_register("Temperature", "READ_ONLY")
    register_map.add_register("Humidity",    "READ_ONLY")
    register_map.add_register("Gyro1",       "READ_ONLY")
    register_map.add_register("Gyro2",       "READ_ONLY")
    register_map.add_register("LEDs",        "READ_WRITE")

    register_map.set_bit_name("LEDs", 0, "Running")
    register_map.set_bit_name("LEDs", 1, "Error")

    # Tell the program where to output the files
    register_map.output_dir = Path(tmpdir) / "maps"

    register_map._set_addresses()

    output_vhdl = vhdl_mapper.create_vhdl(register_map)

    assert output_vhdl == """\
package system is
constant Temperature : integer := 0;
constant Humidity : integer := 4;
constant Gyro1 : integer := 8;
constant Gyro2 : integer := 12;
constant LEDs : integer := 16;
constant Running : integer := 0;
constant Error : integer := 1;
end package system;
"""
