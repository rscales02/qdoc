import logging
import threading
import requests

from datetime import datetime

from flask import Flask, Response

log_format = (
    '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')

logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    filename='../debug.log',
)

api = Flask(__name__)  # create the application instance :)
api.config.from_object(__name__)  # load config from this file , flaskr.py

global DATA


def get_crypto_list():
    print('getting list')
    try:
        with open('crypto_list.txt', 'r') as f:
            coins = f.readlines()
            coins = [x.rstrip() for x in coins]
            return {"data": coins}
    except FileNotFoundError:
        logging.error('File not found')
        return None


crypto_list = get_crypto_list()
api.config['LIST'] = crypto_list['data']


def get_data(c_list):
    print('getting data')
    url = 'https://api.coinbase.com/v2/prices/%s/buy'
    values = {}
    for coin in c_list:
        req = requests.get(url % coin).json()
        if 'data' in req.keys():
            values[coin] = req['data']['amount']

    return values


def periodic():
    print('periodic fetch')
    global DATA
    d_list = api.config['LIST']
    DATA = get_data(d_list)
    logging.debug('Periodic shot!!!!')
    threading.Timer(300, periodic).start()


periodic()


@api.route('/get_data', methods=['GET', 'POST'])
def index():
    global DATA
    if DATA is not None:
        return DATA
    return 'Hello, again, again'


@api.route('/time')
def get_current_time():
    return {'time': datetime.now()}


if __name__ == '__main__':
    api.run()
    log = logging.getLogger(__name__)
