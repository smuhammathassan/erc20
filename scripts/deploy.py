from brownie import AJToken, accounts, network
from web3 import Web3
from scripts.helpful_scripts import get_account

initial_supply = Web3.toWei(1000, "ether")


def main():
    account = get_account()
    AJT = AJToken.deploy(initial_supply, {"from": account})
    print(f"{AJT.name()} is deployed...!")
