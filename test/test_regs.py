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
    new_bit = regs.Bit("new_bit", 0)

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


def test_set_addresses(tmpdir):
    """
    Test that the addresses are set correctly.
    """

    bit_widths = [8, 16, 32, 64, 128, 256, 1024]

    for bit_width in bit_widths:
        word_size_bytes = bit_width / 8

        # Create a new map object with a name and a size
        register_map = regs.Map("system", bit_width)

        # Create the map by adding registers
        register_map.add_register("Temperature", "READ_ONLY")
        register_map.add_register("Humidity",    "READ_ONLY")
        register_map.add_register("Gyro1",       "READ_ONLY")
        register_map.add_register("Gyro2",       "READ_ONLY")
        register_map.add_register("LEDs",        "READ_WRITE")

        register_map._set_addresses()

        # Check addresses are added correctly
        assert register_map.registers["Temperature"].address_offset == 0
        assert register_map.registers["Humidity"].address_offset == word_size_bytes
        assert register_map.registers["Gyro1"].address_offset == word_size_bytes * 2
        assert register_map.registers["Gyro2"].address_offset == word_size_bytes * 3
        assert register_map.registers["LEDs"].address_offset == word_size_bytes * 4


def test_add_bit_map():
    # Create a new map object with a name and a size
    register_map = regs.Map("system", 32)

    register_map.add_register("LEDs", "READ_WRITE")
    register_map.add_bit_map("LEDs", 0, 1, "Running")
    register_map.add_bit_map("LEDs", 1, 1, "Error")
    register_map.add_bit_map("LEDs", 2, 8, "Count")

    assert register_map.registers["LEDs"].bit_groups[0].bits[0].name == "Running"
    assert register_map.registers["LEDs"].bit_groups[1].bits[0].name == "Error"
    assert register_map.registers["LEDs"].bit_groups[2].bits[0].name == "Count_0"
    assert register_map.registers["LEDs"].bit_groups[2].bits[1].name == "Count_1"
    assert register_map.registers["LEDs"].bit_groups[2].bits[2].name == "Count_2"
    assert register_map.registers["LEDs"].bit_groups[2].bits[3].name == "Count_3"
    assert register_map.registers["LEDs"].bit_groups[2].bits[4].name == "Count_4"
    assert register_map.registers["LEDs"].bit_groups[2].bits[5].name == "Count_5"
    assert register_map.registers["LEDs"].bit_groups[2].bits[6].name == "Count_6"
    assert register_map.registers["LEDs"].bit_groups[2].bits[7].name == "Count_7"
