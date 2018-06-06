# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 00:20:45 2018

@author: DELL
"""

# Important libraries to import
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

# Using ggplot design for plottting data
style.use('ggplot')

# Defining start and end timeframe
start = dt.datetime(2001,1,1)
end = dt.datetime(2016,12,31)

# Reading data from web of the stcoks tesla and morningstar
df = web.DataReader('TSLA','morningstar',start,end)
# df.head prints first 5 rows of the database
print(df.head())
# df.tail will print last 5 rows
print(df.tail())