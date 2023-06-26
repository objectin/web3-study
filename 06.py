from web3 import Web3
import json
import requests

# https://ethgasstation.info/

infura_url = 'https://mainnet.infura.io/v3/44ec0d0f28b04d438f34cdc3a9015a5a'
web3 = Web3(Web3.HTTPProvider(infura_url))

req = requests.get('https://ethgasstation.info/json/ethgasAPI.json')
t = json.loads(req.content)

print('safeLow', t['safeLow'])
print('average', t['average'])
print('fast', t['fast'])
print('fastest', t['fastest'])

#web3.eth.Eth.generateGasPrice`
gas_price1 = web3.eth.gas_price
print(gas_price1/10**8)