from app import create_app
import flask_sqlalchemy
import pytest


__name__ = 'tests'


# Given
# @pytest.fixture
def client():
    api = create_app('testing')
    with api.test_request_context(), api.test_client() as c:
        c.environ_base['HTTP_AUTHORIZATION'] = 'Bearer '
        return c
