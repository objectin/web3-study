import streamlit as st
import requests
import time
from web3 import Web3

# Connect to Infura node
infura_url = 'https://mainnet.infura.io/v3/44ec0d0f28b04d438f34cdc3a9015a5a'
web3 = Web3(Web3.HTTPProvider(infura_url))

def fetch_gas_prices():
    req = requests.get('https://ethgasstation.info/json/ethgasAPI.json')
    return req.json()

# reserve slots
safeLow_slot = st.empty()
average_slot = st.empty()
fast_slot = st.empty()
fastest_slot = st.empty()
gas_price_slot = st.empty()

def write_gas_prices():
    t = fetch_gas_prices()

    safeLow_slot.text(f"safeLow: {t['safeLow']}")
    average_slot.text(f"average: {t['average']}")
    fast_slot.text(f"fast: {t['fast']}")
    fastest_slot.text(f"fastest: {t['fastest']}")

    #web3.eth.Eth.generateGasPrice
    gas_price1 = web3.eth.gas_price
    gas_price_slot.text(f"Gas Price: {gas_price1/10**9} Gwei")

def main():
    st.title("Live Ethereum Gas Fees")
    while True:
        write_gas_prices()
        # Streamlit will rerun the script from the top after we've waited a second.
        # This will update the info every 1 second.
        time.sleep(1)

if __name__ == "__main__":
    main()