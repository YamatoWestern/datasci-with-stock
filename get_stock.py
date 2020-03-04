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

def get_yahoo(name):
    stock = pdr.get_data_yahoo(name+'.BK', 
                            start=datetime.datetime(2017, 10, 1), 
                            end=datetime.datetime(2017, 12, 30))
    return stock

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input', type=str,
                        help='given stock name as the input for query')
    args = parser.parse_args()
    print(get_yahoo(args.input))