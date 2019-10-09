import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import statsmodels.api as stat
import statsmodels.tsa.stattools as ts
import statsmodels.tsa.seasonal as sn

import tkinter as tk
from tkinter import filedialog





from dateutil.parser import parse 
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

from numpy import cumsum, log, polyfit, sqrt, std, subtract
from numpy.random import randn


# START COMMON

plt.rcParams['figure.figsize'] = [12, 9]

# convert datetime
lambda_dt = lambda x : pd.datetime.strptime(x, "%d/%m/%Y %H:%M:%S")


# END COMMON


# START IMPORT DATA

root = tk.Tk()
root.withdraw()

file_path1 = filedialog.askopenfilename(initialdir = "/",title = "Select the first quotes file",filetypes = (("csv files","*.csv"),("csv files","*.csv")))

file_path2 = filedialog.askopenfilename(initialdir = "/",title = "Select the second quotes file",filetypes = (("csv files","*.csv"),("csv files","*.csv")))


#load csv data as this track
#Date;Open;High;Low;Close;Volume
#31/12/2009 16:00:00;1,6073;1,6229;1,6041;1,617;53212

dailyQuotes1 = pd.read_csv(file_path1, 
                          sep=';', 
                          decimal=',',
                          header = 0 , 
                          parse_dates=[0], 
                          date_parser = lambda_dt, 
                          index_col='Date')

dailyQuotes1.reset_index(inplace=True)

# change data type from string to 

dailyQuotes1['Close'] = dailyQuotes1['Close'].astype(float)
closes1 = dailyQuotes1['Close'].values



dailyQuotes2 = pd.read_csv(file_path2, 
                          sep=';', 
                          decimal=',',
                          header = 0 , 
                          parse_dates=[0], 
                          date_parser = lambda_dt, 
                          index_col='Date')

dailyQuotes2.reset_index(inplace=True)

# change data type from string to 

dailyQuotes2['Close'] = dailyQuotes2['Close'].astype(float)
closes2 = dailyQuotes2['Close'].values


#debug
#print(dailyQuotes.dtypes)
#print(dates.dtype)

# END IMPORT DATA

result = stat.OLS(closes1,closes2).fit()
check = ts.adfuller(result.resid)

if check[0] <= check[4]['10%'] and check[1] <= 0.1:
    print("Pair of instrument is co-integrated")
else:
    print("Pair of instrument is NOT co-integrated")