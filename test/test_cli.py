from pathlib import Path

from click.testing import CliRunner
from ruamel.yaml import YAML

from context import reg_mapper
from reg_mapper import cli


def test_regmap(tmpdir):
    # Create a test config file
    yaml = YAML()
    config_file = Path("test/config.yaml")
    yaml.dump({
        "outputs": ["vhdl"],
        "vhdl": {
            "output_path": str(tmpdir)
        }
    }, config_file)

    # Test CLI
    runner = CliRunner()
    result = runner.invoke(cli.regmap, ['test/test1.yaml', 'test/test2.yaml', str(config_file)])
    assert result.exit_code == 0

    # Assert output files exist
    test_file_1 = Path(tmpdir) / "map1.vhd"
    test_file_2 = Path(tmpdir) / "map2.vhd"
    assert test_file_1.exists()
    assert test_file_2.exists()
