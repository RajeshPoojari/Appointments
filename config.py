# external
from dotenv import load_dotenv
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cok-gizli-anahtar'
    # DATABASE configurations
    MY_DB_PATH = 'mysql+pymysql://rajesh:Raj@123@localhost:3306/webapp'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or MY_DB_PATH
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    #ADMINS = ['adnankayace@gmail.com']

    # local email server
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['raj.yme@gmail.com']
    # To generate email token
    SECURITY_PASSWORD_SALT = os.environ.get(
        'SECURITY_PASSWORD_SALT') or "SPS#44#"
    # pagination
    POSTS_PER_PAGE = 3
