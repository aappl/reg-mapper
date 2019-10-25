
library IEEE;
use IEEE.std_logic_1164.all;

package ${map_name} is

  -- Registers
  %for register in register_map.registers:
  constant ${register.name} : integer := ${register.address_offset};
  %endfor

  -- Bit maps
  %for register in register_map.registers:
  -- ${register.name} bit map
  %for bit_map in register.bit_maps:
  constant ${register.name}_${bit_map.name} : integer := ${bit_map.start_bit}
  %endfor

  %endfor
end package;
