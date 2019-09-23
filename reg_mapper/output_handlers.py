"""
This file contains functions that create output files in different languages. The output
handler functions are added to a list that can be used to call all of the functions
iteratively.

Output process:
- Get configuration file data.
- Call all output handlers based on input config. Pass each handler the necessary data from the config file.
- Get string of output data from handler and save to output file based on config file data.
"""

from pathlib import Path

from reg_mapper import output_vhdl_package


def write_output(config, data):
    output_path = Path(config["output_path"]) / config["filename"]
    with open(output_path, 'w') as f:
        f.write(data)


output_handlers = []


def vhdl_package_handler(config, system):
    vhdl_package_id = "vhdl"
    if vhdl_package_id in config:
        # TODO Put checks here on the vhdl config
        for register_map in system.register_maps:
            output = output_vhdl_package.create_vhdl_package(register_map)
            write_output(config[vhdl_package_id], output)


output_handlers.append(vhdl_package_handler)


def output_files(config, system):
    for handler in output_handlers:
        handler(config, system)
