# services/users/project/config.py

import os   # new


class BaseConfig:
    """Base configuration"""
    Testing = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # new
    SECRET_KEY = 'my_precious'  # new, update base config
    DEBUG_TB_ENABLED = False               #    new
    DEBUG_TB_INTERCEPT_REDIRECTS = False    # new


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')    # new
    DEBUG_TB_ENABLED = True         # new


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True  # this overwrites the testing variable in parent class
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')   # new


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')    # new
