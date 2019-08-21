import click

from reg_mapper import input_handlers
from reg_mapper import ui


@click.command()
@click.argument('files_in', nargs=-1, type=click.Path(exists=True))  # Get any number of input files
def regmap(files_in):
    """
    help for regmap
    """
    print("hello")
    # Convert input files to dictionaries
    input_dicts = input_handlers.get_dicts(files_in)

    # Add dictionaries to reg_map object
    reg_map = ui.RegMapper()
    for input in input_dicts:
        print(input)
        reg_map.add_map(input)

    # click.echo(reg_map.maps)

    # Create all requested outputs


if __name__ == '__main__':
    regmap()
