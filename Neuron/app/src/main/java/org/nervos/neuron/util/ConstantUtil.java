package org.nervos.neuron.util;

import org.nervos.neuron.util.bip44.PublicKey;
import org.web3j.utils.Numeric;

import java.math.BigInteger;

public class ConstantUtil {

    public static final String ETH = "ETH";
    public static final String NOS = "NOS";

    public static final BigInteger ETHDecimal = new BigInteger("1000000000000000000");
    public static final String ETH_MAIN_NET = "Ethereum Mainnet";
    public static final int ETH_CHAIN_ID = -1;
    public static final String SOURCE_CODE_GITHUB_URL = "https://github.com/cryptape/Neuron-Android";

    // transaction list page config information
    public static final String ETHER_SCAN_API_KEY = "T9GV1IF4V7YDXQ8F53U1FK2KHCE2KUUD8Z";
    public static final String NERVOS_NODE_URL = "http://47.97.171.140:4000";
    public static final String NERVOS_TRANSACTION_URL = NERVOS_NODE_URL + "/api/transactions";
    public static final String ETH_TRANSACTION_URL = "http://api.etherscan.io/api?apikey="
            + ETHER_SCAN_API_KEY + "&module=account&action=txlist&sort=asc&address=";

    // discover page config information
    public static final String DISCOVER_URL = "http://47.97.171.140:8866/dapps";
    public static final String INNER_URL = "http://47.97.171.140:8866/";

    public static final BigInteger NervosDecimal = new BigInteger("100000000000000000");
    public static final String NERVOS_CHAIN_NAME = "Nervos Chain";
    public static final long DEFAULT_NERVOS_DEFAULT_CHAIN_ID = 1;
    public static final long DEFAULT_QUATO = 1000000;
    public static final String NERVOS_NODE_IP = "http://47.94.105.230:1337";
//    public static final String ETH_NODE_IP = "https://mainnet.infura.io/h3iIzGIN6msu3KeUrdlt";
    public static final String ETH_NODE_IP = "https://rinkeby.infura.io/llyrtzQ3YhkdESt2Fzrk";


    public static final BigInteger GAS_LIMIT = Numeric.toBigInt("0x23280");
    public static final BigInteger GAS_PRICE = Numeric.toBigInt("0x4E3B29200");
    public static final String RPC_RESULT_ZERO = "0x";

    public static final String SERVER_URL = "http://118.31.229.67:8000";

    public static final String ZERO_16 = "000000000000000000000000";
    public static final String NAME_HASH = "06fdde03";
    public static final String SYMBOL_HASH = "95d89b41";
    public static final String DECIMALS_HASH = "313ce567";
    public static final String BALANCEOF_HASH = "70a08231";

    public static final long VALID_BLOCK_NUMBER_DIFF = 80L;




    public static final String EXTRA_PAYLOAD = "extra_payload";
    public static final String EXTRA_CHAIN = "extra_chain";


    public static final String CHAIN_ETHEREUM = "ethereum";
    public static final String CHAIN_CITA = "cita";

    public static final String TRANSACTION_SUCCESS = "success";
    public static final String TRANSACTION_DENIED = "denied";
    public static final String TRANSACTION_FAILED = "failed";



}
