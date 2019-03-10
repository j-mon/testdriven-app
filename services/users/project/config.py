# services/users/project/config.py

import os   # new


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    Testing = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # new
    SECRET_KEY = 'my_precious'  # new, update base config
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False    # new
    BCRYPT_LOG_ROUNDS = 13


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')    # new
    DEBUG_TB_ENABLED = True         # new
    BCRYPT_LOG_ROUNDS = 4


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True  # this overwrites the testing variable in parent class
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')   # new
    BCRYPT_LOG_ROUNDS = 4


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # new
