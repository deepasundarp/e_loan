# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:56:33 2019

@author: Deepasundar P
"""
import pandas as pd
from e_loan.loan import Auctioneer


def readfile_df(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def test_orderbook_gets_filled_up():
    buyers_path = "./data/buyers.csv"
    sellers_path = "./data/sellers.csv"
    
    buyers = readfile_df(buyers_path)
    sellers = readfile_df(sellers_path)
    
    buyers = pd.DataFrame(data = [[2, 3], [4, 5]], columns=["", ""])
    
    auctioneer = Auctioneer(buyers, sellers)
    
    allocation = auctioneer.run()
    
    print (auctioneer.bids_FTL)
    
    assert auctioneer.bids_FTL == [1]
