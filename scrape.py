#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 19:37:45 2018
@author: kogito
"""
import requests
from bs4 import BeautifulSoup

r = requests.get('https://coinmarketcap.com/currencies/tron/historical-data/?start=20130428&end=20180421')
soup = BeautifulSoup(r.text, 'lxml')

data = []
table = soup.find('table', id='')
for row in table.find_all('tr'):
    cells = row.findChildren('td')
    values = []
    for cell in cells:
        value = cell.string
        values.append(value)
    try: 
        Date = values[0]
        Open = values[1]
        High = values[2]
        Low =  values[3]
        Close = values[4]
        Volume = values[5]
        MarketCap = values[6]
    except IndexError:
        continue
    data.append((Date, Open, High, Low, Close, Volume, MarketCap))


for item in data:
    print(item)
    
