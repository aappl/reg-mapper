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
    new_bit = regs.Bit(0)
    new_bit.name = "new_bit"

    assert new_bit.name == "new_bit"
    assert new_bit.number == 0


def test_register():
    """
    Test that a register can be created.
    """
    name = "my_reg"
    width = 8

    # Create 8 bit register
    reg = regs.Register(name, width)

    assert reg.name == name
    assert reg._width == width


def test_map(tmpdir):
    """
    Test that a map object can be created.
    """
    # Create a new map object with a name and a size
    register_map = regs.Map("system", 8)

    # Create the map by adding registers
    register_map.add_register("Temperature", "READ_ONLY")
    register_map.add_register("Humidity",    "READ_ONLY")
    register_map.add_register("Gyro1",       "READ_ONLY")
    register_map.add_register("Gyro2",       "READ_ONLY")
    register_map.add_register("LEDs",        "READ_WRITE")

    register_map.set_bit_name("LEDs", 0, "Running")
    register_map.set_bit_name("LEDs", 1, "Error")

    # Check values are added correctly
    assert register_map.registers["Temperature"].name == "Temperature"
    assert register_map.registers["Humidity"].name == "Humidity"
    assert register_map.registers["Gyro1"].name == "Gyro1"
    assert register_map.registers["Gyro2"].name == "Gyro2"
    assert register_map.registers["LEDs"].name == "LEDs"

    assert register_map.registers["Temperature"]._width == 8
    assert register_map.registers["Humidity"]._width == 8
    assert register_map.registers["Gyro1"]._width == 8
    assert register_map.registers["Gyro2"]._width == 8
    assert register_map.registers["LEDs"]._width == 8

    assert register_map.registers["LEDs"].bits[0].name == "Running"
    assert register_map.registers["LEDs"].bits[1].name == "Error"


def test_add_register_exception():
    """
    Test that a value error is raised when an incorrect value is
    given for the rw parameter.
    """
    with pytest.raises(ValueError):
        map = regs.Map()
        map.add_register("test_reg", "Not_Exist")


def test_output_dir():
    """
    Test that the output directory can be set properly and changed.
    """
    reg_map = regs.Map("new_map", 8)

    assert reg_map.output_dir == Path("register_maps")

    reg_map.output_dir = "new_dir"
    assert reg_map.output_dir == Path("new_dir")


def test_base_address():
    """
    Test that the base address can be added correctly to the map
    object.
    """
    reg_map = regs.Map("new_map", 32)
    reg_map.base_address = 16

    assert reg_map.base_address == 16


def test_width_checking():
    """
    Test that the widths of the registers are checked properly.
    """
    with pytest.raises(ValueError):
        reg_map = regs.Map(width=20)
