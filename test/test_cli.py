from pathlib import Path

from click.testing import CliRunner
import cson

from context import reg_mapper
from reg_mapper import cli


def test_regmap(tmpdir):
    # Create a test config file
    config = cson.dumps({"vhdl": {"output_path": str(tmpdir), "filename": "output.vhd"}})
    print(config)
    config_file = Path("test/config.cson")
    with config_file.open("w") as f:
        f.write(config)

    runner = CliRunner()
    result = runner.invoke(cli.regmap, ['test/test.json', 'test/test.cson', str(config_file)])
    # print(dir(result))
    # print(result.stderr)
    print(result.stdout)
    assert result.exit_code == 0
