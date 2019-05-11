"""
test_regs
Test file for the regs module.
"""

from pathlib import Path

import pytest

from context import reg_mapper
from reg_mapper import regs


def test_bit():
    """
    Test that a bit can be created.
    """
    reg = regs.bit("new_bit")

    assert reg.name == "new_bit"


def test_register():
    """
    Test that a register can be created.
    """
    # Create 8 bit register
    reg = regs.register("my_reg", 8)


def test_map(tmpdir):
    """
    Test that a map object can be created.
    """
    # Create a new map object with a name and a size
    register_map = regs.map("system", 8)

    # Create the map by adding registers
    register_map.add_register("Temperature", "READ_ONLY")
    register_map.add_register("Humidity",    "READ_ONLY")
    register_map.add_register("Gyro1",       "READ_ONLY")
    register_map.add_register("Gyro2",       "READ_ONLY")
    register_map.add_register("LEDs",        "READ_WRITE")

    assert register_map.registers[0].name == "Temperature"
    assert register_map.registers[1].name == "Humidity"
    assert register_map.registers[2].name == "Gyro1"
    assert register_map.registers[3].name == "Gyro2"
    assert register_map.registers[4].name == "LEDs"

    assert register_map.registers[0].width == 8
    assert register_map.registers[1].width == 8
    assert register_map.registers[2].width == 8
    assert register_map.registers[3].width == 8
    assert register_map.registers[4].width == 8


def test_add_register_exception():
    """Test that a value error is raised when an incorrect value is given for the rw parameter."""
    with pytest.raises(ValueError):
        map = regs.map()
        map.add_register("test_reg", "Not_Exist")


def test_output_dir():
    """
    Test that the output directory can be set properly and changed.
    """
    reg_map = regs.map("new_map", 8)

    assert reg_map.output_dir == Path("register_maps")

    reg_map.output_dir = "new_dir"
    assert reg_map.output_dir == Path("new_dir")
