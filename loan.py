from typing import List
import csv

def readfile(path: str) -> List[List]:
    
    with open(path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


class FixedTermLoan:
    pass

class Bid:
    def __init__(self, bid):
        self.start = bid[0]
        self.time_cd = bid[1]
        self.load_cd = bid[2]
        self.ramp_cd = bid[3]
        self.serv_period = bid[4]
        self.time_db = bid[5]
        self.load_db = bid[6]
        self.ramp_db = bid[7]
        self.price = bid[7]
'''    
    def _init_(self, start: int, time_cd: int, load_cd: int, ramp_cd: int, 
              serv_period: int, time_db: int, load_db: int, ramp_db: int, 
              price: float):

        self.start = start
        self.time_cd = time_cd
        self.load_cd = load_cd
        self.ramp_cd = ramp_cd
        self.serv_period = serv_period
        self.time_db = time_db
        self.load_db = load_db
        self.ramp_db = ramp_db
        self.price = price
'''
    
        
class Buyer:
    def get_bid(self, bid: List) -> Bid:
        b = Bid(bid)
        return b

    def __init__(self,bid):
        self.bid = Bid(bid)



class Ask:
    def __init__(self, ask: List):
        self.start = ask[0]
        self.time_cd = ask[1]
        self.load_cd = ask[2]
        self.ramp_cd = ask[3]
        self.serv_period = ask[4]
        self.time_db = ask[5]
        self.load_db = ask[6]
        self.ramp_db = ask[3]
#        self.price = ask[3]
'''
    def __init__(self, volume: int, price: float, volume_unit: str, price_unit: str):
        self.volume = volume
        self.price = price
        self.volume_unit = volume_unit
        self.price_unit = price_unit
'''

class Seller:

    def get_ask(self, ask: List) -> Ask:
        return Ask(ask)

    def __init__(self, ask):
        self.ask = Ask(ask)

# %% Class Auctioneer

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
        for bid in self.buyers:
            bids.append(Buyer(bid).bid)
        for s in auctioneer.sellers:
            asks.append(Seller.get_ask(Seller,s))
        allocations = self.match(bids, asks)
#        for a in allocations:
#            a.buyer.send_allocation(self, a)
#            a.seller.send_allocation(self, a)
            
    def __init__(self, buyers: List[Buyer], sellers: List[Seller]):
        self.buyers = buyers
        self.sellers = sellers


# %% Program starts - calling asks and bids

# Asks and bids file are in csv format
buyers_path = "./data/buyers.csv"
sellers_path = "./data/sellers.csv"

buyers = readfile(buyers_path)
sellers = readfile(sellers_path)

auctioneer = Auctioneer(buyers, sellers)

auctioneer.run()
