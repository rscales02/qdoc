import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# import Config
from .config import DevelopmentConfig, TestingConfig

# import models for migration

__version__ = '0.1.0'


# Add logger
logger = logging.getLogger(__name__)
# Config format and stream/file handlers
formatter = logging.Formatter('%(asctime)s| %(levelname)-8s| %(name)-12s| %(message)s')
stream = logging.StreamHandler()
stream.setFormatter(formatter)
# file = RotatingFileHandler('api.log', maxBytes=2000, backupCount=10)
# file.setFormatter(formatter)
# Set log level and add handlers
logger.setLevel(logging.DEBUG)
logger.addHandler(stream)
# logger.addHandler(file)

# Load plugins
db = SQLAlchemy()
login = LoginManager()
migrations = Migrate()


def create_app(config_type=None):
    # Create and configure the application instance :)
    api = Flask(__name__)
    if config_type == 'testing':
        api.config.from_object(TestingConfig)
    else:
        api.config.from_object(DevelopmentConfig)
    # Init plugins manager
    login.init_app(api)
    db.init_app(api)
    migrations.init_app(api, db)

    with api.app_context():
        # import and register blueprints
        db.create_all()
        from app.views.index import index
        from app.views.auth import auth
        api.register_blueprint(index)
        api.register_blueprint(auth)

    return api
