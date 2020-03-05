import argparse, json, sys
from googlefinance import getQuotes

import pandas_datareader as pdr
import datetime

def get_googlefinance(name):
    try:
        symbol = name
        return json.dumps(getQuotes('SET:' + symbol), indent=2)
    except:
        print("Error:", sys.exc_info()[0])
        print("Description:", sys.exc_info()[1])

def get_yahoo(name, from_year, to_year):
    stock = pdr.get_data_yahoo(name+'.BK', 
                            start=datetime.datetime(from_year,1,1), 
                            end=datetime.datetime(to_year,12,31))
    return stock

def load_stock(name):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process the stock data')
    parser.add_argument('input', type=str,
                        help='given stock name as the input for query')
    parser.add_argument('from_year', type=int,
                        help='retrieve data from year')
    parser.add_argument('to_year', type=int,
                        help='retrieve data to year')
    args = parser.parse_args()
    stock = get_yahoo(args.input, args.from_year, args.to_year)
    stock.to_csv(args.input + '-' + str(args.from_year) + '-' + str(args.to_year) + '.csv')