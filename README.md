<h1 align="center">
Solana Sender with Custom RPC
</h1>

This is a solana sending code while the network is congested.

## Requirements

You'll need to obtain API keys for a Custom RPC.

## Installation

1. Clone this repository: `git clone https://github.com/burakhotan/solSender.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Replace the following placeholders in the `config.py.example` file with your API keys, private key and receiver's public key:
4. Rename `config.py.example` as `config.py` and save it

    ```python
      PRIV_KEY = ''
      RECEIVER_PUB_KEY =''
      RPC_URL = ''
    ```
4. Start the bot: `python sendSol.py`

## Authors
- www.github.com/burakhotan

## Disclaimer

This code is provided for educational purposes only and should not be used as financial advice.
