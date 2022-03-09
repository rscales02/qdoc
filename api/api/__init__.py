from flask import Flask
from .config import DevelopmentConfig, TestingConfig

__version__ = '0.1.0'


def create_app(config_type=None):
    # create the application instance :)
    api = Flask(__name__)
    if config_type == 'testing':
        api.config.from_object(TestingConfig)
    else:
        api.config.from_object(DevelopmentConfig)
    from views.main import main
    api.register_blueprint(main)

    return api
