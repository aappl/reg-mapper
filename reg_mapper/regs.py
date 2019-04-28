from enum import Enum

class write_protection(Enum):
    READ_WRITE = 1
    READ_ONLY  = 2


class bit():
    """Class representing one bit in a register."""

    def __init__(self, name, rw=write_protection.READ_WRITE):
        self.name = name
        self.rw   = rw
