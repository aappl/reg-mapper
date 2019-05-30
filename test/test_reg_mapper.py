
import pytest

from context import reg_mapper
from reg_mapper import reg_mapper


def test_RegMapper_inputs():
    regs = reg_mapper.RegMapper("test.json")
    assert isinstance(regs.maps, dict)

    regs = reg_mapper.RegMapper("test.cson")
    assert isinstance(regs.maps, dict)

    regs = reg_mapper.RegMapper({})
    assert isinstance(regs.maps, dict)

    with pytest.raises(TypeError):
        reg_mapper.RegMapper([])
