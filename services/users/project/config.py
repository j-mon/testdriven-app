# services/users/project/config.py

class BaseConfig:
    """Base configuration"""
    Testing = False


class DevelopmentConfig(BaseConfig):
    """Development configuration""" #doc strings for class
    pass


class TestingConfig(BaseConfig):
    """Testing configuration"""
    Testing = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
