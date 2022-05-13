import unittest
from unittest.mock import patch, MagicMock
from app.models import User, Post
from app import db
from . import client


class TestUser(unittest.TestCase):
    def setUp(self, scope='module') -> None:
        self.user = User('test@test.com')
        return super().setUp()

    @patch('app.models.generate_password_hash')
    def test_user_set_password(self, mock_gen_pass_hash):
        # Given mock generated password hash
        mock_gen_pass_hash.side_effect = ['1234']
        # When
        self.user.set_password('1234')
        # Expect
        mock_gen_pass_hash.assert_called_once_with('1234')
        assert self.user.password_hash == '1234'

    @patch('app.models.check_password_hash')
    def test_user_check_password(self, mock_check_pass_hash):
        # Given password and mocked response of werkzug check_password_hash
        self.user.set_password('1234')
        mock_check_pass_hash.side_effect = [True]
        # When
        self.user.check_password('1234')
        # Assert
        mock_check_pass_hash.assert_called_once_with(self.user.password_hash, '1234')

    def test_user_repr(self):
        # Assert
        assert '<User test@test.com>' in repr(self.user)


class TestPost(unittest.TestCase):
    def setUp(self) -> None:
        self.user = MagicMock()
        self.post = Post(body='test text', author=self.user)
        return super().setUp()

    @patch('app.models.User')
    def test_post_content(self, user_cls_mock):
        user_cls_mock.side_effect = [self.user]
        assert "test" in self.post.body
        assert '<Post ' in repr(self.post)
