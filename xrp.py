from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet, Wallet
from xrpl.models.transactions import Payment
from xrpl.utils import xrp_to_drops
import xrpl.account as account
from xrpl.transaction import submit_and_wait
from xrpl.core import addresscodec
from xrpl.models.requests.account_info import AccountInfo


class Server:

    def __init__(self):
        self.JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
        self.client = JsonRpcClient(self.JSON_RPC_URL)
        self.wallet = generate_faucet_wallet(self.client, debug=True)
        self.address = self.wallet.address

    def create_wallet(self) -> Wallet:
        """Returns address of new user wallet."""
        client_wallet = generate_faucet_wallet(self.client, debug=True)
        return client_wallet

    def pay_server(self, wallet: Wallet, amount: float) -> str:
        payment = Payment(
            account=wallet.address,
            amount=xrp_to_drops(amount),
            destination=self.address
        )
        response = submit_and_wait(
            payment, self.client, wallet)
        return response
    
    def pay_client(self, wallet: Wallet, amount: float) -> str:
        payment = Payment(
            account=self.address,
            amount=xrp_to_drops(amount),
            destination=wallet.address
        )
        response = submit_and_wait(
            payment, self.client, self.wallet)
        return response



if __name__ == "__main__":
    server = Server()
    server.register_new_user('olalis')
    server.pay_client('olalis', 20)
    print(account.get_balance(server.address, server.client))
