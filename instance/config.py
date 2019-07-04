import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    DATABASE_URL = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = os.getenv('DATABASE_URL')


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_TEST_URL")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


class ReleaseConfig(Config):
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'release': ReleaseConfig,
    'db_url': "postgres://nxwsoicuofzxvk:bc2ae45ec7aba2409d46c9abe457bf4031cfc752a78828903fa97581866f6ed9@ec2-54-83-1-101.compute-1.amazonaws.com:5432/d7qv96qij463es"
}
