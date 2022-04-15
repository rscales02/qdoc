from . import client

import unittest
import logging
from unittest.mock import patch, MagicMock
# Add logger
logger = logging.getLogger(__name__)
# Config format and stream/file handlers
formatter = logging.Formatter('%(asctime)s| %(levelname)-8s| %(name)-12s| %(message)s')
stream = logging.StreamHandler()
stream.setFormatter(formatter)
# Set log level and add handlers
logger.setLevel(logging.DEBUG)
logger.addHandler(stream)


class TestAuth(unittest.TestCase):

    def setUp(self) -> None:
        self.client = client()
        self.user_data = {'email': 'test@test.com', 'password': 1234}
        self.user_mock = MagicMock()
        return super().setUp()

    @patch('app.views.auth.User')
    @patch('app.views.auth.db')
    def test_register_user(self, db_mock, user_cls_mock):
        # Given
        user_cls_mock.side_effect = [self.user_mock]
        # When
        p = self.client.post('/auth/register', query_string=self.user_data)
        # Assert
        db_mock.session.add.assert_called_with(self.user_mock)
        db_mock.session.add.assert_called_once()
        db_mock.session.commit.assert_called_once()
        self.user_mock.set_password.assert_called_with('1234')
        self.user_mock.set_password.assert_called_once()
        assert p.status_code == 302
        assert b'login' in p.data

    # @patch('app.views.auth.User')
    # @patch('app.views.auth.db')
    # def test_user_login(self, db_mock, user_cls_mock):
    #     user_cls_mock.side_effect = {self.user_mock}
    #     # When registered and logged in
    #     self.client.post('/auth/register', query_string=self.user_data)
    #     self.client.post('/auth/login', query_string=self.user_data)
    #     self.user_mock.check_password.assert_called_with('1234')
    #     self.user_mock.check_password.assert_called_once()
    #
    # @patch('app.views.auth.User')
    # @patch('app.views.auth.db')
    # def test_get_users(self, db_mock, user_cls_mock):
    #     user_cls_mock.side_effect = {self.user_mock}
    #     self.client.post('/auth/register', query_string=self.user_data)
    #     users = self.client.get('/auth/get_users')
    #     logger.info('Testing get_users: %s', users.data.decode('utf-8'))
    #     assert users.status_code == 200
