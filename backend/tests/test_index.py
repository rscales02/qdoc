import unittest
from flask import request, make_response, url_for
from unittest.mock import patch, MagicMock

from . import client


class TestAuth(unittest.TestCase):

    def setUp(self) -> None:
        self.client = client()
        self.user_data = {'email': 'test@test.com', 'password': 1234}
        self.post_mock = MagicMock()
        return super().setUp()

    def test_get_index(self):
        # When User not logged in
        i = self.client.get('/')
        # Expect
        assert i.status_code == 200
        assert b'time' in i.data

    def test_post_post(self):
        # When User logged in
        regis = self.client.post('/auth/register', query_string=self.user_data)
        logresp = self.client.post('/auth/login', query_string=self.user_data)
        cookie = logresp.headers.get('Set-Cookie')
        print(cookie)
        self.client.set_cookie('localhost', cookie)
        p_body = 'gimme money!'
        p_r = self.client.post('/post', body=p_body)
        assert p_r.status_code == 201
