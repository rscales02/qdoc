import logging
from logging.handlers import RotatingFileHandler

import pytest
import json

from api import create_app

# Add logger
logger = logging.getLogger(__name__)
# Config format and stream/file handlers
formatter = logging.Formatter('%(asctime)s| %(levelname)-8s| %(name)-12s| %(message)s')
stream = logging.StreamHandler()
stream.setFormatter(formatter)
stream.setLevel(logging.DEBUG)
file = RotatingFileHandler('test.log', maxBytes=2000, backupCount=10)
file.setFormatter(formatter)
file.setLevel(logging.INFO)
# Set log level and add handlers
logger.addHandler(stream)
logger.addHandler(file)


# Given
@pytest.fixture
def client():
    api = create_app('testing')
    with api.test_client() as client:
        yield client


def test_get_main(client):
    # When post request sent to '/time'
    c_data = client.get('/time')
    # Expect Response.data not to be None
    logger.debug(c_data.data)
    assert c_data.status_code is 200
    # When response received
    res_dict = json.loads(c_data.data.decode('utf-8'))
    # Expect response.data to be bytes dict
    assert isinstance(res_dict, dict)
    assert 'time' in res_dict.keys()


def test_db(client):
    pass
