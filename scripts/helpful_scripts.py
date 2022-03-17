from brownie import accounts, network, config
from idna import check_initial_combiner

FORKED_LOCAL_ENV = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENV = ["development", "ganache-local", "mainnet-fork"]


def get_account(index=None, id=None):
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"])
