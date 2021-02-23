import os

from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_API_KEY = os.environ.get('TWILIO_API_KEY')
    TWILIO_API_SECRET = os.environ.get('TWILIO_API_SECRET')
    TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URI')
        or f"sqlite:///{os.path.join(basedir, 'dev.sqlite')}"
    )


class TestConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    LOGIN_DISABLED = True


config_env_files = {
    'testing': 'eta_notifications_flask.config.TestConfig',
    'development': 'eta_notifications_flask.config.DevelopmentConfig',
    'production': 'eta_notifications_flask.config.DefaultConfig',
}
