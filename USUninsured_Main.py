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

"""
fig = plt.gcf()
fig.set_size_inches(15,10)

plt.plot(df_Uninsured["state"],df_Uninsured["diff"],'b.')

plt.xticks(df_Uninsured["state"],rotation="90")
plt.xlabel("State")
plt.ylabel("Increase in the Uninsured Decrease %")
plt.title("Difference in the Uninsured (under 65 years) Percentage Change Before and After the ACA by US State" )
plt.show()
"""
#------------------------------------------
# Bargraph(stacked) to compare the drop between before and after the ACA.
# Issue: the overlapping area of the bar shows brown.  How to stack without the color change?
#------------------------------------------

Uninsured_BarStacked(df_Uninsured)
"""
fig = plt.gcf()
fig.set_size_inches(15,10)

index = np.arange(51)

opacity = 0.4
bar_width = 0.7

plt.bar(df_Uninsured["state"],df_Uninsured["2010-13"],bar_width,
       alpha=opacity, color='r',
       label="before the ACA")

plt.bar(df_Uninsured["state"],
       df_Uninsured["2013-16"],bar_width,
       alpha=opacity, color='g',
       label="after the ACA")


plt.xlabel("State")
plt.xticks(df_Uninsured["state"], rotation="90")
plt.ylabel("Changes in the Uninsured Percent")
plt.title("Comparison in the Uninsured Percentage Change Before and After the ACA by US State" )
plt.show()
"""
#--------------------------------------------
# Bargraph (side-by-side) to compare the change percentage between before and after the ACA.
# ref: https://matplotlib.org/gallery/statistics/barchart_demo.html.
#--------------------------------------------

Uninsured_BarSideBySide(df_Uninsured)

"""
fig,ax = plt.subplots(figsize=(15,10))

index = np.arange(51)

opacity = 0.4
bar_width = 0.35

ax.bar(index,df_Uninsured["2010-13"],bar_width,
       alpha=opacity, color='r',
       label="before the ACA")

ax.bar(index+bar_width,
       df_Uninsured["2013-16"],bar_width,
       alpha=opacity, color='g',
       label="after the ACA")

ax.set_xlabel("State")
ax.set_xticks(index+bar_width/2)
ax.set_ylabel("Changes in the Uninsured Percentage")
ax.set_title("Comparison in the Uninsured (under 65 years) Percentage Change Before and After the ACA by US State" )
ax.set_xticklabels(state_codes)
ax.legend()   # to show the bar labels
fig.tight_layout()  # make subplots fit within the figure
plt.show()
"""