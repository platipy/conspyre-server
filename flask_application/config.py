#!/usr/bin/env python

# http://flask.pocoo.org/docs/config/#development-production
import base64

class Config(object):
    SECRET_KEY = 'My Secret Key'
    SITE_NAME = 'Conspyre Server' + ' @ University of Delaware'
    SITE_ROOT_URL = 'http://example.com' #TODO
    MEMCACHED_SERVERS = ['localhost:11211']
    SYS_ADMINS = ['foo@example.com']
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


    #configured for GMAIL
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'email@email.email'
    MAIL_PASSWORD = base64.b64decode('') # Might be 'FY29yeUJhcnQwOw==FYWNiME9TQzs='
    DEFAULT_MAIL_SENDER = 'Admin < admin@email.email >'
    
    SECURITY_CONFIRMABLE = False
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_URL_PREFIX = "/auth"

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECURITY_CONFIRMABLE = True
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = False

class TestConfig(Config):
    SITE_ROOT_URL = 'http://localhost:5000'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    SITE_ROOT_URL = 'http://localhost:5000'
    '''Use "if app.debug" anywhere in your code, that code will run in development code.'''
    #DEBUG = False
    #TESTING = True

