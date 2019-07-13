# external
from dotenv import load_dotenv
import os


# internal
import smtplib


BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or MY_DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'raj.yme@gmail.com'
    MAIL_PASSWORD = '9908470955'
    ADMINS = 'raj.yme@gmail.com'

    # local email server
    #MAIL_SERVER = os.environ.get('MAIL_SERVER')
    #MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    #MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    #MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    #MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    #ADMINS = ['raj.yme@gmail.com']
    # To generate email token
    SECURITY_PASSWORD_SALT = os.environ.get(
        'SECURITY_PASSWORD_SALT') or 'bcrypt'
    # pagination
    #POSTS_PER_PAGE = 3
