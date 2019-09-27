from pathlib import Path

from click.testing import CliRunner
import cson

from context import reg_mapper
from reg_mapper import cli


def test_regmap(tmpdir):
    # Create a test config file
    config = cson.dumps({"vhdl": {"output_path": str(tmpdir), "filename": "output.vhd"}})
    config_file = Path("test/config.cson")
    with config_file.open("w") as f:
        f.write(config)

    # Test CLI
    runner = CliRunner()
    result = runner.invoke(cli.regmap, ['test/test.json', 'test/test.cson', str(config_file)])
    assert result.exit_code == 0

    # Assert output files exist
    test_file_1 = Path(tmpdir) / "map1.vhd"
    test_file_2 = Path(tmpdir) / "map2.vhd"
    assert test_file_1.exists()
    assert test_file_2.exists()
