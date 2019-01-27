""" Imports """

from typing import List
import csv
import pandas as pd
from pandas import DataFrame

# %%
""" User functions """
def readfile(path: str) -> List[List]:
    
    with open(path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def readfile_df(path: str) -> DataFrame:
    df = pd.read_csv(path)
    return df

# %% 
""" Classes Ask and Bid """
class Bid:
    def __init__(self, bid: pd.Series):
        self.buyer_id = bid["buyer_id"]
        self.start = bid["start"]
        self.time_cd = bid["time_cd"]
        self.load_cd = bid["load_cd"]
        self.ramp_cd = bid["ramp_cd"]
        self.serv_period = bid["serv_period"]
        self.time_db = bid["time_db"]
        self.load_db = bid["load_db"]
        self.ramp_db = bid["ramp_db"]
        self.price = bid["price"]
 
class Ask:
    def __init__(self, ask: pd.Series):
        self.buyer_id = ask["seller_id"]
        self.start = ask["start"]
        self.time_cd = ask["time_cd"]
        self.load_cd = ask["load_cd"]
        self.ramp_cd = ask["ramp_cd"]
        self.serv_period = ask["serv_period"]
        self.time_db = ask["time_db"]
        self.load_db = ask["load_db"]
        self.ramp_db = ask["ramp_db"]
        self.price = ask["price"]
# %% 
"""Classes for different categories of loans"""
class FixedTermLoan:
    pass

class VariableTermLoan:
    pass

class NetZeroProfileLoan:
    pass

class NetZeroVariableTermLoan:
    pass

# %% 
"""Class Auctioneer """

class Auctioneer:
    """Trade mediator that matches bids and asks of participating traders.
    The Auctioneer actively pulls bids and asks from Buyer and Seller objects,
    and actively pushes allocations to them."""

    def match(self, bids: list, asks: list) -> list:
        """Clearing process that matched bids with asks.
        Returns allocation."""
        # Todo: write matching algorithm
        return []

    def run(self):
        """A single marker run that consists of collecting bids and asks, running the clearing process
        and communicating the resulting allocations to the participating traders."""
        bids = []
        asks = []
        for index,b in self.buyers.iterrows():
            bids.append(Bid(b))
        for index, s in self.sellers.iterrows():
            asks.append(Ask(s))
        allocations = self.match(bids, asks)
        for a in allocations:
            a.buyer.send_allocation(self, a)
            a.seller.send_allocation(self, a)
            
    def __init__(self, buyers: DataFrame, sellers: DataFrame):
        self.buyers = buyers
        self.sellers = sellers


# %% 
""" Program starts - calling asks and bids """

""" Asks and bids file are in csv format """
buyers_path = "./data/buyers.csv"
sellers_path = "./data/sellers.csv"

buyers = readfile_df(buyers_path)
sellers = readfile_df(sellers_path)

auctioneer = Auctioneer(buyers, sellers)

auctioneer.run()

