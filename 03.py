# Test your connection to the Ethereum blockchain using Web3.py and Python

from web3 import Web3

infura_url = 'https://mainnet.infura.io/v3/44ec0d0f28b04d438f34cdc3a9015a5a'
web3 = Web3(Web3.HTTPProvider(infura_url))

isConnected = web3.is_connected()

blocknumber = web3.eth.block_number

print(isConnected, blocknumber)

balance = web3.eth.get_balance('0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B') # 비탈릭 부테린 지갑주소
print(balance)

balance = web3.eth.get_balance('0x5DCA270671935cf3dF78bd8373C22BE250198a03') # 세겔 파이낸스
print(balance)

# BSC Mainnet
# Connect to Binance Mainnet
w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))

# Address of the wallet to check balance for
wallet_address = '0x232981987E3620F83983E2e3743cC200154D06E8'

# Get the balance in BNB (Binance Coin)
balance_in_wei = w3.eth.get_balance(wallet_address)
balance_in_bnb = w3.from_wei(balance_in_wei, 'ether')

# Print the balance
print(f"Wallet balance: {balance_in_bnb} BNB")
