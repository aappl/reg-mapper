
from pathlib import Path
import json

import cson

class RegMapper():
    """The user interface to the Register Mapper library."""

    def __init__(self, reg_maps):
        self.maps = None

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
