# -*- coding: utf-8 -*-
"""
Created on Thu May 10 20:24:01 2018

@author: bsuzow

USUninsured_main.py

This project conducts an exploratory data analysis on the US Uninsured population.  The 3 data sets are retrieved from the US Census Bureau (See readme.text for the URLs).

Since the ACA was signed into law in 2010 by President Obama, its major provisions had taken into effect by 2014. Wikeppedia reports "the uninsured share of population had roughtly halved." 

We will 1) confirm the report, 2) discover the top and bottom 5 states in terms of decrease ratios.
 
"""

import pandas as pd

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

from US_States import GetStateCodes
from USUninsured_Plots import *

#-----------------------------------
# Read the sheets of the xls file.
#-----------------------------------

fname = "USUninsured.xls"

df2010 = pd.read_excel(fname,sheet_name='2010')
df2013 = pd.read_excel(fname,sheet_name='2013')
df2016 = pd.read_excel(fname,sheet_name='2016')

diff10_13 = df2013["UnInsu%"] - df2010["UnInsu%"]

diff13_16 = df2016["UnInsu%"] - df2013["UnInsu%"]

diff = diff10_13 - diff13_16

state_codes = GetStateCodes()

#--------------------------------------
# A quick scatterplot:
#   Red dots for the % change from 2010 to 2013
#   Green dots for from 2013 to 2016
# This is not the best way to communicate although green dots are scattered below red dots for all states implying that the uninsured  had decreased since most of the ACA provisions had gone into full effects.
#--------------------------------------
fig = plt.gcf()
fig.set_size_inches(12,8)

plt.plot(state_codes,diff10_13,'r.')
plt.plot(state_codes,diff13_16,'g.')
plt.xticks(state_codes,rotation="vertical")
plt.xlabel("State")
plt.ylabel("Decrease in %")
plt.title("The Uninsured % Decrease by US State" )
plt.show()

#----------------------------------------------
# Combine the 10-13 and 13-16 change rates into a single df for plotting.
#----------------------------------------------

df_Uninsured = pd.DataFrame(dict(s1=diff10_13, s2=diff13_16, s3=diff, s4=state_codes))

df_Uninsured.columns = ["2010-13","2013-16","diff","state"]

with open("USUninsuredACA.csv","w") as csvfile:
    df_Uninsured.to_csv(csvfile)

#------------------
# Run t-test.
#------------------

stats.ttest_rel(diff10_13, diff13_16)

t_criticalVal = stats.t.ppf((1-.975),df=100)
# cdf is the inverse of ppf
p_val = stats.t.cdf(t_criticalVal,df=100)

#--------------------------------------
# Scatterplot the difference in the percentage change by state.
#--------------------------------------

Uninsured_Scatterplot(df_Uninsured)


#------------------------------------------
# Bargraph(stacked) to compare the drop between before and after the ACA.
# Issue: the overlapping area of the bar shows brown.  How to stack without the color change?
#------------------------------------------

Uninsured_BarStacked(df_Uninsured)

#--------------------------------------------
# Bargraph (side-by-side) to compare the change percentage between before and after the ACA.
# ref: https://matplotlib.org/gallery/statistics/barchart_demo.html.
#--------------------------------------------

Uninsured_BarSideBySide(df_Uninsured)

