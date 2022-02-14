import logging
from datetime import date, datetime

from flask import Flask, Response

from api.get_data import get_data

log_format = (
    '[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s')

logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    filename='../debug.log',
)

api = Flask(__name__)  # create the application instance :)
api.config.from_object(__name__)  # load config from this file , flaskr.py

# Load default config and override config from an environment variable
api.config.update(dict(
    FILE='crypto_list.txt'
))

FILE = api.config['FILE']


def get_crypto_list(file=FILE):
    try:
        with open(file, 'r') as f:
            coins = f.readlines()
            coins = [x.rstrip() for x in coins]
            return {"data": coins}
    except FileNotFoundError:
        logging.error('File not found')
        return None


@api.route('/get_data', methods=['GET', 'POST'])
def index():
    c_list = get_crypto_list()
    ticker = get_data(c_list['data'])
    if ticker is not None:
        resp = ticker
        print(resp)
        return resp
    return 'Hello, again, again'


@api.route('/get_list', methods=['GET'])
def get_list():
    c_list = get_crypto_list()
    if c_list is not None:
        return c_list
    else:
        return Response(status=404)


@api.route('/time')
def get_current_time():
    return {'time': datetime.now()}


if __name__ == '__main__':
    api.run()
    log = logging.getLogger(__name__)
