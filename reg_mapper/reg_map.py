
class Map():
    """
    Class to hold the register map data, and to provide a generic interface
    for other components to get data about the map.
    """

    def __init__(self, maps):
        self.maps = maps

    def get_reg_numbers(self, reg_map):
        """
        Get a dictionary of register names with addresses assigned.
        """
        reg_nums = {}
        address = 0
        for register, _ in self.maps[reg_map]["registers"].items():
            reg_nums[register] = address
            address += 1

        return reg_nums

    def get_bits(self, reg_map, register):
        """
        Get a dictionary of bit names with start numbers and widths.
        """
        bits = {}
        for bit, _ in self.maps[reg_map]["registers"][register]["bits"].items():
            bits[bit] = self.maps[reg_map]["registers"][register]["bits"][bit]
        return bits
