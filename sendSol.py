from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solana.rpc.api import Client
from solders.system_program import TransferParams, transfer
from solana.transaction import Transaction
import base58
import config

sender = Keypair.from_base58_string(config.PRIV_KEY)
receiver = config.RECEIVER_PUB_KEY
receiver_converted = Pubkey(base58.b58decode(receiver))

def send_Sol(sender,receiver,amount):
     amountInLamports = int(amount * 1000000000)
     
     transfer_ix = transfer(TransferParams(from_pubkey=sender.pubkey(), to_pubkey=receiver, lamports=amountInLamports))
     txn = Transaction().add(transfer_ix)
     solana_client = Client(config.RPC_URL)
     receipt = solana_client.send_transaction(txn, sender)
     print(receipt)

send_Sol(sender,receiver_converted,1)
