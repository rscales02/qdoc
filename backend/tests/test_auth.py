from . import client
from sqlite3 import IntegrityError

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


class TestRegister(TestAuth):
    def setUp(self) -> None:
        return super().setUp()

    @patch('app.views.auth.User')
    @patch('app.views.auth.db')
    def test_register_user(self, db_mock, user_cls_mock):
        # Given new User class creation
        user_cls_mock.side_effect = [self.user_mock]
        # When
        p = self.client.post('/auth/register', query_string=self.user_data)
        # Assert
        user_cls_mock.assert_called_once()
        self.user_mock.set_password.assert_called_once_with('1234')
        db_mock.session.add.assert_called_with(self.user_mock)
        db_mock.session.add.assert_called_once()
        db_mock.session.commit.assert_called_once()
        assert p.status_code == 201
        assert b'login' in p.data

    def test_register_without_query_string(self):
        # When
        p = self.client.post('/auth/register')
        # Assert
        assert p.status_code == 400
        assert b'Missing' in p.data

    @patch('app.views.auth.User')
    def test_register_user_already_exists(self, user_cls_mock):
        # Given SQL IntegrityError meaning email already exists
        user_cls_mock.side_effect = [IntegrityError]
        # When
        p = self.client.post('/auth/register', query_string=self.user_data)
        # Assert
        assert p.status_code == 409
        assert b'User already exists' in p.data


class TestLogin(TestAuth):
    def setUp(self) -> None:
        return super().setUp()

    def test_user_login_no_query_string(self):
        # When
        p = self.client.post('/auth/login')
        # Assert
        assert p.status_code == 400

    @patch('app.views.auth.set_access_cookies')
    @patch('app.views.auth.User.query.filter_by')
    @patch('app.views.auth.create_access_token', return_value='<JWT Token>')
    @patch('app.views.auth.User')
    def test_user_login(self, user_cls_mock, mock_create_token, mock_filter_call, mock_set_cookie):
        # Given User query call returning User instance
        mock_filter_call.return_value.first.side_effect = [self.user_mock]
        # When
        p = self.client.post('/auth/login', query_string=self.user_data)
        # Assert
        mock_create_token.assert_called_once_with(identity=self.user_mock.email)
        mock_filter_call.assert_called_once()
        self.user_mock.check_password.assert_called_once_with('1234')
        assert p.status_code == 200

    @patch('app.views.auth.User.query.filter_by')
    @patch('app.views.auth.User')
    def test_user_login_wrong_email(self, user_cls_mock, mock_filter_call):
        # Given User query call returning User instance
        mock_filter_call.return_value.first.side_effect = [None]
        # When
        p = self.client.post('/auth/login', query_string=self.user_data)
        # Assert
        assert p.status_code == 401

    @patch('app.views.auth.User.query.filter_by')
    @patch('app.views.auth.User')
    def test_user_login_wrong_password(self, user_cls_mock, mock_filter_call):
        # Given User query call returning User instance
        mock_filter_call.return_value.first.side_effect = [self.user_mock]
        self.user_mock.check_password.return_value = False
        # When
        p = self.client.post('/auth/login', query_string={'email': 'test@test.com', 'password': 4321})
        # Assert
        self.user_mock.check_password.assert_called_with('4321')
        assert p.status_code == 401

    def test_get_users(self):
        users = self.client.get('/auth/get_users')
        assert users.status_code == 200
        assert b'Empty' in users.data
