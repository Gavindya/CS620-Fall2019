"""
CS 620
HW2-b
@author: Gavindya Jayawardena (UIN-01130618)
"""

import pandas as pd
import urllib.request
import xmltodict
import numpy as np

def read_csv(csv_url):
    return  pd.read_csv(csv_url)

def read_xml(xml_url):
    file = urllib.request.urlopen(xml_url)
    return xmltodict.parse(file.read())

def unique_symbols(csv_data):
    return csv_data['Symbol'].unique()

def ticker_find(xml_dict, ticker):
    xml_df = pd.DataFrame(xml_dict.get('symbols').get('symbol'))
    if xml_df[xml_df['@ticker']==ticker]['@name'].empty:
        return " No data in SP500"
    return xml_df[xml_df['@ticker']==ticker]['@name'].to_string(index=False)

def calc_avg_open(csv_data, ticker):
    return np.around(np.mean(csv_data.loc[csv_data['Symbol']==ticker]['Open']),decimals=2)

def vwap(csv_data, ticker):
    df = csv_data.loc[csv_data['Symbol'] == ticker]
    df['vwap'] = ((df['High'] + df['Low'] + df['Close']) / 3) * df['Volume']
    sum_vwap = np.sum(df['vwap'])
    sum_volume = np.sum(df['Volume'])
    return np.around((sum_vwap/sum_volume),decimals=2)


xml_url = 'https://www.cs.odu.edu/~sampath/courses/f19/cs620/files/data/SP500_symbols.xml'
csv_url = "https://www.cs.odu.edu/~sampath/courses/f19/cs620/files/data/SP500_ind.csv"
xml_dict = read_xml(xml_url)
csv_data = read_csv(csv_url)
tickers = unique_symbols(csv_data)

print(tickers)
df = pd.DataFrame()
df['ticker'] = tickers

df['avg_open'] = df['ticker'].apply(lambda x: calc_avg_open(csv_data,x))
df['vwap'] = df['ticker'].apply(lambda x: vwap(csv_data,x))

print(df)

for t in tickers:
    print('%s %s %s' % (ticker_find(xml_dict,t),
                          df.loc[df['ticker']==t]['avg_open'].to_string(index=False),
                          df.loc[df['ticker']==t]['vwap'].to_string(index=False)))