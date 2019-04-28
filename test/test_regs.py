from context import reg_mapper

def test_regs():
    reg = reg_mapper.bit("new_bit")

    assert reg.name == "new_bit"
    assert reg.rw   == reg_mapper.write_protection.READ_WRITE
