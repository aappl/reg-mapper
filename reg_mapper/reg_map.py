
class Map():
    """
    Class to hold the register map data, and to provide a generic interface
    for other components to get data about the map.
    """

    def __init__(self, maps):
        self.maps = maps

    def get_reg_numbers(self):
        reg_map_nums = {}
        for reg_map, _ in self.maps.items():
            address = 0
            reg_nums = {}
            for register, _ in self.maps[reg_map]["registers"].items():
                reg_nums[register] = address
                address += 1

            reg_map_nums[reg_map] = reg_nums

        return reg_map_nums
