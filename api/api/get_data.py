import requests


def get_data(c_list):
    url = 'https://api.coinbase.com/v2/prices/%s/buy'
    values = {}
    for coin in c_list:
        req = requests.get(url % coin).json()
        if 'data' in req.keys():
            values[coin] = req['data']['amount']
            
    return values
