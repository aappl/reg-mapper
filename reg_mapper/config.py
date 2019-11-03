
from reg_mapper import input_handlers


class Config():
    """
    Contains all configuraion information for the register mapper.
    """

    def __init__(self, config_file_path):
        self.reg_map_file_paths = None
        self.output_paths = None
        self.output_generators = None

        self._read_config(config_file_path)

    def _read_config(self, config_file_path):
        """
        Read config file and fill in the attributes of this object.
        """
        # Convert YAML input to python dict
        config = input_handlers.get_dicts([config_file_path])[0]

        self.reg_map_file_paths = config["register_maps"]
        self.output_paths = dict(config["output_paths"])
        self.output_generators = config["output_generators"]
