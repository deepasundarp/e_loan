""" Imports """

import pandas as pd
from pandas import DataFrame

# %%
""" User functions """
def readfile_df(path: str) -> DataFrame:
    df = pd.read_csv(path)
    return df


# %% 
""" Classes Ask and Bid """
class Bid:
    def __init__(self, bid: pd.Series):
        self.buyer_id = bid["buyer_id"]
        self.loan_type = bid["loan_type"]
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
        self.seller_id = ask["seller_id"]
        self.loan_type = ask["loan_type"]
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

def FixedTermLoan(bids: list, asks:list) -> DataFrame:
    
    index = []
    columns = []
    for b in bids:
        index.append(b.buyer_id)
    for a in asks:
        columns.append(a.seller_id)
        
    matches = DataFrame(index = index, columns = columns)

    for b in bids:
        for a in asks:
            if (b.start == a.start) and \
                (b.time_cd == a.time_cd) and \
                (b.load_cd == a.load_cd) and \
                (b.ramp_cd == a.ramp_cd) and \
                (b.serv_period == a.serv_period) and \
                (b.time_db == a.time_db) and \
                (b.load_db == a.load_db) and \
                (b.ramp_db == a.ramp_db) and \
                (b.price <= a.price):
                
                matches.loc[b.buyer_id][a.seller_id] = (a.price + b.price) / 2
            
            else:
                pass
    return matches
            
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
    def __init__(self, buyers: DataFrame, sellers: DataFrame):
        self.buyers = buyers
        self.sellers = sellers

    def match(self, bids: list, asks: list) -> list:
        """Clearing process that matched bids with asks.
        Returns allocation."""
        self.matches = DataFrame()
        self.bids = bids
        self.asks = asks
        self.bids_FTL = []
        self.bids_VTL = []
        self.asks_FTL = []
        self.asks_VTL = []
        
        for b in self.bids:
            getattr(self, "bids_%s" % b.loan_type).append(b)
            
        for a in self.asks:
            getattr(self, "asks_%s" % a.loan_type).append(a)
                  
        return FixedTermLoan(self.bids_FTL, self.asks_FTL)

    def run(self):
        """A single marker run that consists of collecting bids and asks, running the clearing process
        and communicating the resulting allocations to the participating traders."""
        bids = []
        asks = []
        for index,b in auctioneer.buyers.iterrows():
            bids.append(Bid(b))
        for index, s in self.sellers.iterrows():
            asks.append(Ask(s))
        allocations = self.match(bids, asks)

        return allocations


# %% 
""" Program starts - calling asks and bids """

""" Asks and bids file are in csv format """
buyers_path = "./data/buyers.csv"
sellers_path = "./data/sellers.csv"

buyers = readfile_df(buyers_path)
sellers = readfile_df(sellers_path)

auctioneer = Auctioneer(buyers, sellers)

allocations = auctioneer.run()

