from click.testing import CliRunner

from context import reg_mapper
from reg_mapper import cli


def test_regmap():
    runner = CliRunner()
    result = runner.invoke(cli.regmap, ['test/test.json', 'test/test.cson'])
    assert result.exit_code == 0
