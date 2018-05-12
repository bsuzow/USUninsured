# -*- coding: utf-8 -*-
"""
Created on Fri May 11 18:18:09 2018

@author: bsuzow
USUninsured_Plots.py

Functions for plots
"""

def Uninsured_Scatterplot(df):
    """
    Scatterplot the difference in the % changes by state.
    Argument:
        df: data frame with columns named:
            state
            2010-13 
            2013-16
            diff: (2010-2013) minus (2013-16)
    """
    import matplotlib.pyplot as plt

    fig = plt.gcf()
    fig.set_size_inches(15,10)
    
    plt.plot(df["state"],df["diff"],'b.')
    
    plt.xticks(df["state"],rotation="90")
    plt.xlabel("State")
    plt.ylabel("Increase in the Uninsured Decrease %")
    plt.title("Difference in the Uninsured (under 65 years) Percentage Change Before and After the ACA by US State" )
    plt.show()

def Uninsured_BarStacked(df):
    """
    # Bargraph(stacked) to compare the drop between before and after the ACA.
    # Issue: the overlapping area of the bar shows brown.  How to stack without the color change?
    """
    import matplotlib.pyplot as plt
    
    
    fig = plt.gcf()
    fig.set_size_inches(15,10)
    
    opacity = 0.4
    bar_width = 0.7
    
    plt.bar(df["state"],df["2010-13"],bar_width,
           alpha=opacity, color='r',
           label="before the ACA")
    
    plt.bar(df["state"],df["2013-16"]
           ,bar_width,
           alpha=opacity, color='g',
           label="after the ACA")
    
    
    plt.xlabel("State")
    plt.xticks(df["state"], rotation="90")
    plt.ylabel("Changes in the Uninsured Percent")
    plt.title("Comparison in the Uninsured Percentage Change Before and After the ACA by US State" )
    plt.show()

def Uninsured_BarSideBySide(df):
    """
    Bargraph (side-by-side) to compare the change percentage between before and after the ACA.
    ref: https://matplotlib.org/gallery/statistics/barchart_demo.html.
    """
    import matplotlib.pyplot as plt
    import numpy as np
    
    fig,ax = plt.subplots(figsize=(15,10))
    
    index = np.arange(51)
    
    opacity = 0.4
    bar_width = 0.35
    
    ax.bar(index,df["2010-13"],bar_width,
           alpha=opacity, color='r',
           label="before the ACA")
    
    ax.bar(index+bar_width,
           df["2013-16"],bar_width,
           alpha=opacity, color='g',
           label="after the ACA")
    
    ax.set_xlabel("State")
    ax.set_xticks(index+bar_width/2)
    ax.set_ylabel("Changes in the Uninsured Percentage")
    ax.set_title("Comparison in the Uninsured (under 65 years) Percentage Change Before and After the ACA by US State" )
    ax.set_xticklabels(df["state"])
    ax.legend()   # to show the bar labels
    fig.tight_layout()  # make subplots fit within the figure
    plt.show()
