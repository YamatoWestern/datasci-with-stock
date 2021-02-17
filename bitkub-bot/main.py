import json
import time

from bitkub-api.py import *


def load_config():
    with open('config.py', 'r' as f):
        configs = json.load(f)

def func():
    print(configs['API_KEY'])
    print(configs['API_SECRET'])

if __name__ == '__main__':
    while True:
        load_config()
        func()
        time.sleep(60)