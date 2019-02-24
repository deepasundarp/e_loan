# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 14:05:06 2019

@author: Deepasundar P
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import datetime
from collections import deque
import matplotlib.patches as patches

path = "../data/NZP_data/"
dir_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data', 'NZP_data'))
dirs = os.listdir(path)

for i in range(2):
    
    #Variable Definitions:
        #time = hours or days
        #val_acc = realized accumulated consumption over the period
        #val_opt = optimal baseline value over the period
    
    #Plotting Baseline Case 1- Longterm (30 days)
    if i==0:
        df = pd.read_csv(path+dirs[i])
        val_acc = df.val_acc
        time = df.time
        val_opt = np.linspace(0,val_acc[len(val_acc)-1],len(time))
        
        fig, (ax) = plt.subplots(1, 1, sharex=True)
        plt.title("Net Zero Profile Loan - Baseline Case 1")
        plt.xlabel("Days")
        plt.ylabel("Accumulated Energy Consumption (MWh)")

    #Plotting Baseline Case 2- Shortterm (within a day)        
    if i==1:
        df = pd.read_csv(path+dirs[i])
        val_acc = df.val_acc
        time = df.time
        val_opt = df.val_opt

        fig, (ax) = plt.subplots(1, 1, sharex=True)
        plt.title("Net Zero Profile Loan - Baseline Case 2")
        plt.xlabel("Hours")
        plt.ylabel("Accumulated Energy Consumption (kWh)")        

        
    
    #Plotting the curves
    
    acc, =ax.plot(time, val_acc, color='red', linewidth=2.5, label='Actual Consumption')
    opt, =ax.plot(time, val_opt, color='green', linewidth=2.5, label='Optimal Consumption')
    first_legend = plt.legend(handles=[acc, opt], loc="lower right")
    ax1 = plt.gca().add_artist(first_legend)
    
    #Plotting Area fill
    ax.fill_between(time, val_acc, val_opt, where=val_acc >= val_opt, facecolor='blue', interpolate=True)
    ax.fill_between(time, val_acc, val_opt, where=val_acc < val_opt, facecolor='magenta', interpolate=True)
    blue_patch = patches.Patch(color='blue', label='Over consumption than committed')
    magenta_patch = patches.Patch(color='magenta', label='Reduced consumption than committed')
    plt.legend(handles=[blue_patch, magenta_patch])

