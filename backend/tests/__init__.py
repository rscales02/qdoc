from app import create_app

__name__ = 'tests'


# Given
def client():
    api = create_app('testing')
    with api.test_request_context(), api.test_client() as c:
        return c
