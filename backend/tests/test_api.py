import logging
from logging.handlers import RotatingFileHandler

import json
import unittest
from flask import session

from . import client


class TestAuth(unittest.TestCase):

    def setUp(self) -> None:
        self.client = client()
        return super().setUp()

    def test_get_main(self):
        # When post request sent to '/time'
        user_data = {'email': 'test@test.com', 'password': '1234'}
        self.client.post('/register', query_string=user_data)
        self.client.post('/login', query_string=user_data)
        c_data = self.client.get('/time')
        # Expect Response.data not to be None
        assert c_data.status_code == 302
        # When response received
        res_dict = c_data.data.decode('utf-8')
        # Expect response.data to be bytes dict
        # assert isinstance(res_dict, dict)
        # assert 'time' in res_dict.keys()
