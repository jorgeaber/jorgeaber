import os


class Config():
    DEBUG = os.environ['DEBUG']
    DEVELOPMENT = os.environ['DEVELOPMENT']
    TESTING = os.environ['TESTING']
    SECRET_KEY = os.environ['SECRET_KEY']
