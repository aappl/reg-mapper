import click

from reg_mapper import input_handlers
from reg_mapper import output_handlers
from reg_mapper import ui


@click.command()
@click.argument('files_in', nargs=-1, type=click.Path(exists=True))  # Get any number of input files
@click.argument('config_in', nargs=1, type=click.Path(exists=True))
def regmap(files_in, config_in):
    """
    help for regmap
    """
    # Convert input files to dictionaries
    input_dicts = input_handlers.get_dicts(files_in)
    config = input_handlers.get_dicts([config_in])  # TODO fix having to have this as a list

    # Add dictionaries to reg_maps object
    reg_maps = ui.RegMapper()
    for input in input_dicts:
        reg_maps.add_map(input)

    # Create all requested outputs
    output_handlers.output_files(config[0], reg_maps.system)


if __name__ == '__main__':
    regmap()
