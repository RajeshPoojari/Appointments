# external
from datetime import datetime
# internal
from myapp import db


class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(40), nullable=False)
    lname = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    email_confirmed = db.Column(db.Boolean, default=False)

    bookings = db.relationship('Booking', backref='client', lazy='dynamic')

    def __repr__(self):
        return "<Client %r>" % (self.fname+" "+self.lname)

    def full_name(self):
        return self.fname+" "+self.lname

    @classmethod
    def get_client_by_email(cls, email):
        return Client.query.filter_by(email=email).first()


# To save services which are booked in booking
service_booked = db.Table(
    'service_booked',
    db.Column('booking_id', db.Integer, db.ForeignKey('booking.id')),
    db.Column('service_id', db.Integer, db.ForeignKey('service.id'))
)

# To save services which are provided in booking
service_provided = db.Table(
    'service_provided',
    db.Column('booking_id', db.Integer, db.ForeignKey('booking.id')),
    db.Column('service_id', db.Integer, db.ForeignKey('service.id'))
)


class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    is_cancel = db.Column(db.Boolean, default=False)
    cancelation_reason = db.Column(db.String(200))
    booked_datetime = db.Column(db.DateTime, default=datetime.now())
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    total_price = db.Column(db.Integer)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    activated = db.Column(db.Boolean, default=False)

    booked_services = db.relationship('Service', secondary=service_booked)
    provided_services = db.relationship('Service', secondary=service_provided)

    def fill_booked_services(self, id_list):
        """fills booked_services by given service ids """
        for id in id_list:
            s = Service.query.get(id)
            self.booked_services.append(s)

    def fill_provided_services(self, id_list):
        """fills provided_services by given service ids """
        for id in id_list:
            s = Service.query.get(id)
            self.provided_services.append(s)


class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)

    @classmethod
    def total_price_of_selected_services(cls, id_list):
        total_price = 0
        for id in id_list:
            total_price += int(db.session.query(cls.price)
                               .filter_by(id=id).first()[0])
        return total_price
