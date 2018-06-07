# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 12:05:42 2018

@author: DELL
"""

# Important libraries to import
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

df = pd.read_csv('TSLA.csv', parse_dates=True,index_col=0)

# Making a new column in our database(File) after volume column
# min_periods will take average of the days il the number of rows in the table is less 
# than 100 dynamically.
df['100ma']= df['Open'].rolling(window=100,min_periods=0).mean()
# Dropping the rows which have a NAN value in any column
df.dropna(inplace=True)
print(df.head())
print(df.tail())

# Plotting the 
ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)

ax1.plot(df.index, df['Open'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])


