import os


class Config(object):
    SECRET_KEY = 'my_secret_key'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/flask'
# motor://usuario:password@servidor/bd