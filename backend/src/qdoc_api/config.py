import os
import tempfile

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    # SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    db_f, db_path = tempfile.mkstemp()
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, db_path)
    TESTING = True
