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


def write_output(output_path, data):
    # Make sure the output directory exists
    output_dir = output_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create file
    with output_path.open("w") as f:
        f.write(data)


output_handlers = []


def vhdl_package_handler(config, system):
    vhdl_package_id = "vhdl"
    print(config)
    if vhdl_package_id in config["outputs"]:
        # TODO Put checks here on the vhdl config
        for register_map in system.register_maps:
            output = output_vhdl_package.create_vhdl_package(register_map)
            output_path = Path(config[vhdl_package_id]["output_path"]) / (register_map.name + ".vhd")
            write_output(output_path, output)


output_handlers.append(vhdl_package_handler)


def output_files(config, system):
    for handler in output_handlers:
        handler(config, system)
