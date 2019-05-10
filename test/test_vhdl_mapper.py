from context import reg_mapper
from reg_mapper import regs
from reg_mapper import vhdl_mapper

from pathlib import Path


def test_create(tmpdir):
    # Create a new map object with a name and a size
    register_map = regs.map("system", 8)

    # Create the map by adding registers
    register_map.add_register("Temperature", "READ_ONLY")
    register_map.add_register("Humidity",    "READ_ONLY")
    register_map.add_register("Gyro1",       "READ_ONLY")
    register_map.add_register("Gyro2",       "READ_ONLY")
    register_map.add_register("LEDs",        "READ_WRITE")

    # Tell the program where to output the files
    register_map.output_dir = Path(tmpdir) / "maps"

    vhdl_mapper.create(register_map)

    assert 0
