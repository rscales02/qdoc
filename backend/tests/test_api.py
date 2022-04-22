# import logging
# from logging.handlers import RotatingFileHandler
#
# import json
# import unittest
# from flask import session
# from unittest.mock import patch, MagicMock
#
# from . import client
#
#
# class TestAuth(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.client = client()
#         self.user_data = {'email': 'test@test.com', 'password': 1234}
#         self.user_mock = MagicMock()
#         return super().setUp()
#
#     @patch('app.views.auth.User')
#     @patch('app.views.auth.db')
#     def test_get_main(self, db_mock, user_cls_mock):
#         # When User not logged in
#         t = self.client.get('/time')
#         # Expect
#         assert t.status_code == 302
#         assert b"/auth/register" in t.data
#         # # When User logged in
#         # r = self.client.post('/auth/register', query_string=self.user_data)
#         # l = self.client.post('/auth/login', query_string=self.user_data)
#         # print(l)
