#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 19:37:45 2018
@author: kogito
"""
import csv
import requests
from bs4 import BeautifulSoup
import plotly.graph_objs as go


class Scraper():

    def process(self, url):
        r = requests.get(url)
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
            data.append([Date, Open, High, Low, Close, Volume, MarketCap])
        
        for item in data:
            print(item)
        return data
        
    def write_to_csv(self, data):
        f = open('ScrapedData.csv', 'w')
        with f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'MarketCap'])
        
            for row in data:
                writer.writerow(row)
