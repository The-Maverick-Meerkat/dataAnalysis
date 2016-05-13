import quandl
import pandas as pd
import pickle
from matplotlib import style

api_key = 'MtMS-NBs54bNdFK9ij-a'

def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df = df.resample('M', how='sum')
    return df

def sp500_data():
    df = quandl.get("YAHOO/INDEX_GSPC", trim_start="1975-01-01", authtoken=api_key)

    df["Adjusted Close"] = (df["Adjusted Close"]-df["Adjusted Close"][0]) / df["Adjusted Close"][0] * 100.0
    # print(df.head())
    df2 = pd.DataFrame(df["Adjusted Close"])
    df2.resample('M')
    # print(df2.head())
    return df2

def gdp_data():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df = df.resample('M', how='sum')
    # print(df.head())
    return df

def us_unemployment():
    df = quandl.get("ECPI/JOB_G", trim_start="1975-01-01", authtoken=api_key)
    df["Unemployment Rate"] = (df["Unemployment Rate"]-df["Unemployment Rate"][0]) / df["Unemployment Rate"][0] * 100.0
    df = df.resample('M', how='sum')
    return df

HPI_data = pd.read_pickle('pickle2.pickle')

HPI = pd.DataFrame(HPI_data)
# print(HPI_data.head())

m30 = mortgage_30y()
m30.columns = ['M30']
# print(m30.head())
sp500 = sp500_data()
sp500.columns = ['sp500']
# print(sp500.head())
gdp = gdp_data()
gdp.columns = ['GDP']
# print(gdp.head())
unemployment = us_unemployment()
# print(unemployment.head())

HPI2 = HPI.join([m30, sp500, gdp, unemployment])

HPI2.dropna(inplace=True)

print(HPI2.head())

print(HPI.corr())

HPI.to_pickle('HPI.pickle')