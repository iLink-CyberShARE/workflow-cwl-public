import os

class Config:
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")
    USER_DATABASE_URL = os.getenv('USER_DATABASE_URL', "this-is-the-default-URL") 
    POOL_PRE_PING = True
    POOL_SIZE = 10
    POOL_RECYCLE= 3600   
    DEBUG = True
    TESTING = False

class TestingConfig(Config):
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")
    USER_DATABASE_URL = os.getenv("USER_DATABASE_URL", "this-is-the-default-URL") 
    POOL_PRE_PING = True
    POOL_SIZE = 10
    POOL_RECYCLE= 3600   
    DEBUG = True
    TESTING = True

class DevelopmentConfig(Config):
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")
    USER_DATABASE_URL = os.getenv("USER_DATABASE_URL", "this-is-the-default-URL") 
    POOL_PRE_PING = True
    POOL_SIZE = 5
    POOL_RECYCLE= 3600   
    DEBUG = True
    TESTING = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
