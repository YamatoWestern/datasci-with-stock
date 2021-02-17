import json
import time

from bitkub_caller import *


configs = [None]

def load_config():
    with open('config.json', 'r') as f:
        configs[0] = json.load(f)


def func():
    c = url_caller(URL_API)
    print(c.get_obj())


if __name__ == '__main__':
    load_config()
    while True:
        func()
        time.sleep(60)