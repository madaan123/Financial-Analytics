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
df = web.DataReader("TSLA", 'morningstar', start, end)
# df.head prints first 5 rows of the database
print(df.head())
# df.tail will print last 5 rows
print(df.tail())

# Dropping the first column of the tesla symbl from the dataset
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

# Converting the results to a csv file
df.to_csv('TSLA.csv')

# Reading data from a csv file to plot it
df = pd.read_csv('tsla.csv', parse_dates=True,index_col=0)
#print(df.head())
# Plotting the data on a graph
df.plot()

# Plotting only a particular column of the csv file 
df['Open'].plot()

# PLotting multiple columns of our choice
df[['High','Low']]

