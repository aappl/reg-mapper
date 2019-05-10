from context import reg_mapper
from reg_mapper import regs

from pathlib import Path
import pytest

def test_bit():
    reg = regs.bit("new_bit")

    assert reg.name == "new_bit"


def test_register():
    # Create 8 bit register
    reg = regs.register("my_reg", 8)


def test_map(tmpdir):
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

    # Output file types based on the list given
    register_map.create(["vhdl", "c", "html"])


def test_add_register_exception():
    """Test that a value error is raised when an incorrect value is given for the rw parameter."""
    with pytest.raises(ValueError):
        map = regs.map()
        map.add_register("test_reg", "Not_Exist")


def test_output_dir():
    reg_map = regs.map("new_map", 8)

    assert reg_map.output_dir == Path("register_maps")

    reg_map.output_dir = "new_dir"
    assert reg_map.output_dir == Path("new_dir")
