import logging

from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# import Config
from app.config import DevelopmentConfig, TestingConfig


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
migrations = Migrate()
jwt = JWTManager()


def create_app(config_type=None):
    # Create and configure the application instance :)
    api = Flask(__name__)
    if config_type == 'testing':
        api.config.from_object(TestingConfig)
    else:
        api.config.from_object(DevelopmentConfig)
    # Init plugins manager
    db.init_app(api)
    migrations.init_app(api, db)
    jwt.init_app(api)

    @api.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @api.route('/*', methods=["OPTIONS"])
    def options():
        return "OK"

    @jwt.invalid_token_loader
    def unauthorized_callback():
        return redirect(url_for('auth.register'))

    with api.app_context():
        # import and register blueprints
        db.create_all()
        from .views.index import bp as index_bp
        from .views.auth import bp as auth_bp
        api.register_blueprint(index_bp)
        api.register_blueprint(auth_bp)
    return api
