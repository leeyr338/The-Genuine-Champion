#!/bin/bash

export PATH=/Users/leeyr/Documents/cryptape/code/cita-cli/target/debug:$PATH

# compile contacts
rm *.bin
solcjs worldCupGaming.sol --bin &> compile.log


odds=0000000000000000000000000000000000000000000000000000000000000020\
0000000000000000000000000000000000000000000000000000000000000002\
000000000000000000000000000000000000000000000000000000000000000a\
0000000000000000000000000000000000000000000000000000000000000001

contract_bin=0x`cat worldCupGaming_sol_worldCupGaming.bin`$odds;
echo "$contract_bin";

# deploy contract
cita-cli rpc sendRawTransaction --code $contract_bin --private-key 0xb0c33c376f1a99652421f17741cfddbcfcd970ffe4ed1e9d8e99893c26e01036 --url http://47.94.105.230:1337 --quota 1000000000
