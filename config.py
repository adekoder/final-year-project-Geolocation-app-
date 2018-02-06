import os
import hashlib
baseDir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = hashlib.md5().hexdigest()
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://adekoder:adekoder@localhost/yabatech'  

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
            os.path.join(baseDir, 'test.db')


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'default': DevConfig
} 