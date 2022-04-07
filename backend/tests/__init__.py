import pytest
import os

from app import create_app

__name__ = 'tests'


# Given
def client():
    api = create_app('testing')
    with api.test_request_context(), api.test_client() as client:
        return client
    try:
        os.remove(api.config['SQLALCHEMY_DATABASE_URI'])
    except FileNotFoundError:
        pass
