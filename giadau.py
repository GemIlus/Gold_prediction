import csv
import requests


url = 'https://www.alphavantage.co/query'
params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': 'USO',
    'apikey': '80JB7IZPJH68FGRP',
    'outputsize': 'full',
}


response = requests.get(url, params=params)
data = response.json()


start_date = '2022-07-24'
end_date = '2023-03-14'
prices = {}
for date, values in data['Time Series (Daily)'].items():
    if date >= start_date and date <= end_date:
        prices[date] = float(values['4. close'])
uso = []
for key, value in prices.items():
    temp = [key,value]
    uso.append(value)
with open('1.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for value in uso:
        csvwriter.writerow([value])

