#external
from flask import Blueprint

bp = Blueprint('home', __name__)

from myapp.home import routes, models