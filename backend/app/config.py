import os
import tempfile
import logging

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

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    db_f, db_path = tempfile.mkstemp()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, db_path)
    TESTING = True
