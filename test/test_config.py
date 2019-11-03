
from context import reg_mapper
from reg_mapper import config


def test_config():
    config_file_path = "./test/test_config.yaml"

    system_config = config.Config(config_file_path)

    reg_map_file_paths = system_config.reg_map_file_paths
    output_paths = system_config.output_paths
    output_generators = system_config.output_generators

    assert reg_map_file_paths == ["./test_map_1.yaml", "./test_map_2.yaml"]
    assert output_paths == {
        "default": "./default_outputs",
        "c_header": "./c_outputs/"
    }
    assert output_generators == ["vhdl_package", "c_header"]
