# external
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime
# internal
from myapp import db, login
from myapp.home.models import Booking

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password_hashed = db.Column(db.String(128), nullable=False, unique=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    bookings = db.relationship('Booking', backref='employee')

    def __repr__(self):
        return "<User %r>" % self.username

    def set_password(self, password):
        self.password_hashed = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hashed, password)

    def full_name(self):
        return self.fname+" "+self.lname


@login.user_loader
def load_user(id):
    """ for current_user session """
    return User.query.get(int(id))
