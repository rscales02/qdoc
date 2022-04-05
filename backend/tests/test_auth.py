from more_itertools import side_effect
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
        return super().setUp()

    @patch('qdoc_api.views.auth.User')
    @patch('qdoc_api.views.auth.db')
    def test_register_user(self, db_mock, user_cls_mock):
        # Given
        user_data = {'email': 'test@test.com', 'password': 1234}
        user_mock = MagicMock()
        user_cls_mock.side_effect = [user_mock]
        # When
        self.client.post('/auth/register', query_string=user_data)
        # Assert
        db_mock.session.add.assert_called_with(user_mock)
        db_mock.session.add.assert_called_once()
        db_mock.session.commit.assert_called_once()
        user_mock.set_password.assert_called_with('1234')
        user_mock.set_password.assert_called_once()

    def test_get_users(self):
        users = self.client.get('/auth/get_users')
        assert users.status_code == 200
