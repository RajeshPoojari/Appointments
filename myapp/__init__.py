# external
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask import request
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
# internal
from config import Config

""" creates app """
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'auth.login'

from myapp import utils
from myapp.home import models
from myapp.auth import models


from myapp.errors import bp as errors_bp
app.register_blueprint(errors_bp)
from myapp.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')
from myapp.home import bp as home_bp
app.register_blueprint(home_bp)

# if not app.debug and not app.testing:
#     # EMAIL operations
#     if app.config['MAIL_SERVER']:
#         auth = None
#         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
#             auth = (app.config['MAIL_USERNAME'],
#                     app.config['MAIL_PASSWORD'])
#         secure = None
#         if app.config['MAIL_USE_TLS']:
#             secure = ()
#         mail_handler = SMTPHandler(
#             mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
#             fromaddr='sender-adnan@' + app.config['MAIL_SERVER'],
#             toaddrs=app.config['ADMINS'], subject='Booking Hata',
#             credentials=auth, secure=secure)
#         mail_handler.setLevel(logging.ERROR)
#         app.logger.addHandler(mail_handler)

#     # LOGGING operations
#     if not os.path.exists('logs'):
#         os.mkdir('logs')
#     file_handler = RotatingFileHandler(
#         'logs/booking.log', maxBytes=10240, backupCount=10)
#     file_handler.setFormatter(logging.Formatter(
#         '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
#     ))
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)

#     app.logger.setLevel(logging.INFO)
#     app.logger.addHandler('infoce booking')


# def create_app(config_class=Config):
#     """ creates app """
#     app = Flask(__name__)
#     app.config.from_object(config_class)

#     db.init_app(app)
#     migrate.init_app(app, db)
#     login.init_app(app)
#     mail.init_app(app)
#     bootstrap.init_app(app)

#     from myapp.errors import bp as errors_bp
#     app.register_blueprint(errors_bp)

#     from myapp.auth import bp as auth_bp
#     app.register_blueprint(auth_bp, url_prefix='/auth')

#     from myapp.home import bp as home_bp
#     app.register_blueprint(home_bp)

#     # if not app.debug and not app.testing:
#     #     # EMAIL operations
#     #     if app.config['MAIL_SERVER']:
#     #         auth = None
#     #         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
#     #             auth = (app.config['MAIL_USERNAME'],
#     #                     app.config['MAIL_PASSWORD'])
#     #         secure = None
#     #         if app.config['MAIL_USE_TLS']:
#     #             secure = ()
#     #         mail_handler = SMTPHandler(
#     #             mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
#     #             fromaddr='sender-adnan@' + app.config['MAIL_SERVER'],
#     #             toaddrs=app.config['ADMINS'], subject='Booking Hata',
#     #             credentials=auth, secure=secure)
#     #         mail_handler.setLevel(logging.ERROR)
#     #         app.logger.addHandler(mail_handler)

#     #     # LOGGING operations
#     #     if not os.path.exists('logs'):
#     #         os.mkdir('logs')
#     #     file_handler = RotatingFileHandler(
#     #         'logs/booking.log', maxBytes=10240, backupCount=10)
#     #     file_handler.setFormatter(logging.Formatter(
#     #         '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
#     #     ))
#     #     file_handler.setLevel(logging.INFO)
#     #     app.logger.addHandler(file_handler)

#     #     app.logger.setLevel(logging.INFO)
#     #     app.logger.addHandler('infoce booking')
#     # We have to return 'app' !!!
#     return app
