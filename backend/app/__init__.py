import logging

from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, set_access_cookies, get_jwt
from flask_cors import CORS
from datetime import datetime, timezone, timedelta

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
cors = CORS(supports_credentials=True)


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
    cors.init_app(api)

    @jwt.invalid_token_loader
    @jwt.unauthorized_loader
    def unauthorized_callback():
        return redirect(url_for('auth.register'))

    # Using an `after_request` callback, we refresh any token that is within 30
    # minutes of expiring. Change the timedeltas to match the needs of your application.
    @api.after_request
    def refresh_expiring_jwts(response):
        try:
            exp_timestamp = get_jwt()["exp"]
            now = datetime.now(timezone.utc)
            target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
            if target_timestamp > exp_timestamp:
                access_token = create_access_token(identity=get_jwt_identity())
                set_access_cookies(response, access_token)
            return response
        except (RuntimeError, KeyError):
            # Case where there is not a valid JWT. Just return the original respone
            return response

    with api.app_context():
        # import and register blueprints
        db.create_all()
        from .views.index import bp as index_bp
        from .views.auth import bp as auth_bp
        api.register_blueprint(index_bp)
        api.register_blueprint(auth_bp)
    return api
