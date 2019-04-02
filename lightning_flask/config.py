import os
import platform
import json

if platform.system() != 'Windows':
    with open('/etc/config.json') as config_file:
        config = json.load(config_file)


class Config:
    if platform.system() == 'Windows':
        SECRET_KEY = os.environ.get('SECRET_KEY')
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')  # the 3 slashes are a relative path from the current file
        MAIL_SERVER = 'smtp.googlemail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        MAIL_USERNAME = os.environ.get('EMAIL_USER')
        MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    
    else:
        SECRET_KEY = config.get('SECRET_KEY')
        SQLALCHEMY_DATABASE_URI = config.get('SQLALCHEMY_DATABASE_URI')  # the 3 slashes are a relative path from the current file
        MAIL_SERVER = 'smtp.googlemail.com'
        MAIL_PORT = 587
        MAIL_USE_TLS = True
        MAIL_USERNAME = config.get('EMAIL_USER')
        MAIL_PASSWORD = config.get('EMAIL_PASS')