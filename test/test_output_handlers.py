from pathlib import Path

from context import reg_mapper
from reg_mapper import output_handlers
import test_utils


def test_output_files(tmpdir):
    system = test_utils.create_test_object()
    config = {
        "vhdl": {
            "output_path": tmpdir,
        },
        "c": {
            "output_path": tmpdir
        }
    }
    output_handlers.output_files(config, system)

    filename = system.register_maps[0].name + ".vhd"
    output_file = tmpdir / filename
    assert output_file.exists()

    with open(output_file, 'r') as f:
        assert f.read() == """package test_map is

  constant test_register0 : integer := 0;
  constant test_register0_test_register0_bit_map0_0 : integer := 0;
  constant test_register0_test_register0_bit_map0_1 : integer := 1;
  constant test_register0_test_register0_bit_map0_2 : integer := 2;
  constant test_register0_test_register0_bit_map0_3 : integer := 3;
  constant test_register0_test_register0_bit_map1_0 : integer := 4;
  constant test_register0_test_register0_bit_map1_1 : integer := 5;
  constant test_register0_test_register0_bit_map1_2 : integer := 6;
  constant test_register0_test_register0_bit_map1_3 : integer := 7;

  constant test_register1 : integer := 1;
  constant test_register1_test_register1_bit_map0_0 : integer := 0;
  constant test_register1_test_register1_bit_map0_1 : integer := 1;
  constant test_register1_test_register1_bit_map0_2 : integer := 2;
  constant test_register1_test_register1_bit_map0_3 : integer := 3;
  constant test_register1_test_register1_bit_map1_0 : integer := 4;
  constant test_register1_test_register1_bit_map1_1 : integer := 5;
  constant test_register1_test_register1_bit_map1_2 : integer := 6;
  constant test_register1_test_register1_bit_map1_3 : integer := 7;

end package test_map;
"""
