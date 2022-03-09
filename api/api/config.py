class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///stelo.db'


class ProductionConfig(Config):
    FLASK_ENV = 'production'
    # SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://stelo_test.db'
    TESTING = True
