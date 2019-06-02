"""
This is this top level user interface for the reg_mapper project.
"""


from pathlib import Path
import json

import cson

from reg_mapper import regs


class RegMapper():
    """
    The user interface to the Register Mapper library.
    """

    def __init__(self, reg_maps):
        self.maps = None
        self.map_objs = {}

        if isinstance(reg_maps, str):
            reg_file = Path(reg_maps)
            if not reg_file.exists():
                raise FileNotFoundError(reg_file)

            if reg_file.suffix == ".json":
                with open(reg_maps, 'r') as f:
                    json_data = f.read()
                    self.maps = json.loads(json_data)

            elif reg_file.suffix == ".cson":
                with open(reg_maps, 'r') as f:
                    cson_data = f.read()
                    self.maps = cson.loads(cson_data)

        elif isinstance(reg_maps, dict):
            self.maps = reg_maps

        else:
            raise TypeError("{} invalid: Valid types are string or dictionary".format(type(reg_maps)))

        self._create_maps()
        self._set_addresses()

    def _create_maps(self):
        """
        Fill the map_objs variable with register maps.
        """
        # For each register map in the input
        for map, _ in self.maps.items():
            # Create a new Map object
            self.map_objs[map] = regs.Map(map, self.maps[map]["width"])

            # Add all of the registers in the map to the new object
            for reg, _ in self.maps[map]["registers"].items():
                self.map_objs[map].add_register(reg, self.maps[map]["registers"][reg]["RW"])

                # Add all of the bit maps in the register to the new object
                if "bits" in self.maps[map]["registers"][reg]:
                    for bit, _ in self.maps[map]["registers"][reg]["bits"].items():
                        self.map_objs[map].add_bit_map(
                            reg,
                            self.maps[map]["registers"][reg]["bits"][bit]["start_bit"],
                            self.maps[map]["registers"][reg]["bits"][bit]["width"],
                            bit
                        )

                # Add the description to the new object
                if self.maps[map]["registers"][reg]["description"]:
                    self.map_objs[map].add_register_description(
                        reg,
                        self.maps[map]["registers"][reg]["description"]
                    )

    def _set_addresses(self):
        """
        Set the addresses of all the registers in the maps.
        """
        for reg_map, _ in self.map_objs.items():
            self.map_objs[reg_map].set_addresses()
