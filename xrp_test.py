from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet
from xrpl.models.transactions import Payment
from xrpl.utils import xrp_to_drops
import xrpl.account as account
from xrpl.transaction import submit_and_wait
from xrpl.core import addresscodec
from xrpl.models.requests.account_info import AccountInfo

JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)
server_wallet = generate_faucet_wallet(client, debug=True)
print(server_wallet)

client_wallet = generate_faucet_wallet(client, debug=True)
print(client_wallet)


server_account = server_wallet.address
client_account = client_wallet.address
print('prev client:', account.get_balance(address = client_account, client = client))
print('prev server:', account.get_balance(address = server_account, client = client))
my_tx_payment = Payment(
    account = client_account,
    amount=xrp_to_drops(1),
    destination="rPT1Sjq2YGrBMTttX4GZHjKu9dyfzbpAYe",
)
tx_response = submit_and_wait(my_tx_payment, client, client_wallet)
print('post client:', account.get_balance(address = client_account, client = client))
print('post server:', account.get_balance(address = server_account, client = client))
test_xaddress = addresscodec.classic_address_to_xaddress(client_account, tag=12345, is_test_network=True)
print("\nClassic address:\n\n", client_account)
print("X-address:\n\n", test_xaddress)

acct_info = AccountInfo(
    account=client_account,
    ledger_index="validated",
    strict=True,
)
response = client.request(acct_info)
result = response.result
print("response.status: ", response.status)
import json
print(json.dumps(response.result, indent=4, sort_keys=True))
