import pytest
import json

from flask import Response

from api.api import api


# Given
@pytest.fixture
def client():
    with api.test_client() as client:
        yield client


def test_get_crypto_list(client):
    # When get request sent to /get_list
    c_list = client.get('/get_list')
    # Expect response code 200 for successful reading of file
    assert isinstance(c_list, Response)
    assert c_list.status_code == 200


def test_get_ticker_data(client):
    # When post request sent to '/'
    c_data = client.get('/get_data')
    # Expect Response.data not to be None
    assert c_data.data is not None
    # When response received
    res_dict = json.loads(c_data.data.decode('utf-8'))
    # Expect response.data to be bytes dict
    assert isinstance(res_dict, dict)
