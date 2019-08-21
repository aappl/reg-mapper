"""
test_regs
Test file for the regs module.
"""

from pathlib import Path

import pytest

from context import reg_mapper
from reg_mapper import regs
from reg_mapper import exceptions


def test_bit():
    """
    Test that a bit can be created.
    """
    new_bit = regs.Bit("new_bit", 0)

    assert new_bit.name == "new_bit"
    assert new_bit.number == 0


def test_bitmap():
    """
    Test that a BitMap object can be created and have its attributes set.
    """
    # Create some test values
    name = "new_bitmap"
    start_bit = 5
    width = 5
    description = "I'm a test bit map :)"

    # Create test object
    new_bitmap = regs.BitMap()
    new_bitmap.name = name
    new_bitmap.start_bit = start_bit
    new_bitmap.width = width
    new_bitmap.description = description
    new_bitmap.generate_bits()

    # Assert contents are correct
    assert new_bitmap.name == name
    assert new_bitmap.start_bit == start_bit
    assert new_bitmap.width == width
    assert new_bitmap.description == description

    for number, bit in enumerate(new_bitmap.bits):
        assert bit.name == name + "_" + str(number)
        assert bit.number == number + start_bit


def test_register():
    """
    Test that a Register object has the correct default types
    """
    reg = regs.Register()

    assert reg.name is None
    assert reg.rw == "READ_ONLY"
    assert reg.description == ""
    assert reg.bit_maps == []
    assert reg.address_offset is None


def test_check_bit_maps_exception():
    """
    Test that the bit maps will find exceptions correctly.
    """
    reg = regs.Register()
    reg.name = "Test reg"

    # Test overlapping bit map
    bit_map0 = regs.BitMap()
    bit_map0.name = "bit_map0"
    bit_map0.start_bit = 0
    bit_map0.width = 5
    bit_map0.generate_bits()
    bit_map1 = regs.BitMap()
    bit_map1.name = "bit_map1"
    bit_map1.start_bit = 2
    bit_map1.width = 5
    bit_map1.generate_bits()

    # Insert bit maps into register
    reg.bit_maps.append(bit_map0)
    reg.bit_maps.append(bit_map1)

    # Check that an exception is created for the overlapping bit maps
    with pytest.raises(exceptions.BitAssignmentError):
        reg.check_bit_maps()


def test_check_bit_maps():
    """
    Test that the bit maps will be checked for overlapping correctly.
    """
    reg = regs.Register()
    reg.name = "Test reg"

    # Test overlapping bit map
    bit_map0 = regs.BitMap()
    bit_map0.name = "bit_map0"
    bit_map0.start_bit = 0
    bit_map0.width = 5
    bit_map0.generate_bits()
    bit_map1 = regs.BitMap()
    bit_map1.name = "bit_map1"
    bit_map1.start_bit = 5
    bit_map1.width = 5
    bit_map1.generate_bits()

    # Insert bit maps into register
    reg.bit_maps.append(bit_map0)
    reg.bit_maps.append(bit_map1)

    # Check bit maps are checked without an exception
    reg.check_bit_maps()


def test_map_defaults():
    """
    Test that the attributes of the Map object are present and correct.
    """
    map = regs.Map()

    assert map.name is None
    assert map.width is None
    assert map.registers == []
    assert map.base_address is None


def test_map_set_addresses():
    """
    Test that the addresses in the registers can be set correctly with
    the set_addresses method.
    """
    VALID_WIDTHS = [8, 16, 32, 64, 128, 256, 512, 1024]

    for width in VALID_WIDTHS:
        map = regs.Map()
        map.width = width

        # Fill map with registers
        for i in range(10):
            map.registers.append(regs.Register())

        map.set_addresses()

        word_size_bytes = map.width/8
        addr_count = 0
        for reg in map.registers:
            assert reg.address_offset == addr_count
            addr_count += word_size_bytes
            print(addr_count)
