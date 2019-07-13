# -*- coding: utf-8 -*-
# external
from flask import render_template, flash, redirect, url_for, request
# from flask_login import current_user, login_user, logout_user, login_required
# from werkzeug.urls import url_parse
import datetime
# internal
from myapp import db, app 
from myapp.home import bp
from myapp.home.forms import BookingForm
from myapp.home.models import Service, service_provided, service_booked, Client, Booking
from myapp.utils import send_confirmation_token, convert_to_datetime, send_bill_mail
from myapp.utils import generate_token, verify_token
from myapp.auth.models import User
from myapp.home.models import Client

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    form = BookingForm()
    services = Service.query.all()
    employees = User.query.all()
    if form.validate_on_submit():
        fname = form.fname.data
        lname = form.lname.data
        phone = form.phone.data
        email = form.email.data
        str_date = request.form['date']
        str_time = request.form['time']
        start_time = convert_to_datetime(str_date, str_time)
        end_time = start_time + datetime.timedelta(hours=1)
        selected_services = request.form.getlist('selected_services')
        total_price = Service.total_price_of_selected_services(
            selected_services)

        
        # Check if client is already saved
        client = Client.get_client_by_email(email)
        if client is None:
            client = Client(fname=fname, lname=lname, phone=phone, email=email)
            db.session.add(client)
            booking = Booking(start_time=start_time, end_time=end_time,
                              total_price=total_price, client=client)
            booking.fill_booked_services(selected_services)
            db.session.add(booking)
            db.session.commit()
            # SEND EMAIL CONFIRMATION
            send_confirmation_token(client)
            flash("Check your email to verify your email", "warning")
        else:
            booking = Booking(start_time=start_time, end_time=end_time,
                              total_price=total_price, client=client)
            booking.fill_booked_services(selected_services)
            # Booking Activate
            booking.activated = True
            db.session.add(booking)
            db.session.commit()
            # Send bill email
            send_bill_mail(client, booking)
            flash("Check your email", "warning")
        return redirect(url_for('home.index'))
    return render_template('home/index.html', title="Home page", form=form, services=services)


@bp.route('/confirm_email/<token>', methods=['GET', 'POST'])
def confirm_email(token):
    # check token if it belongs to the correct email address
    email = verify_token(token)
    if not email:
        flash('Email verification request incorrect', 'danger')
        return redirect(url_for('home.index'))
    client = Client.query.filter_by(email=email).first_or_404()
    if client.email_confirmed == False:
        client.email_confirmed = True
        booking = Booking.query.filter_by(client_id=client.id).first()
        booking.activated = True
        db.session.commit()
        flash("You have verified your email address, your appointment has been saved", 'success')
        send_bill_mail(client, booking)
    return redirect(url_for('home.index'))


@bp.route('/about_us')
def about_us():
    return render_template('home/about_us.html', title="About Us")


@bp.route('/contact_us')
def contact_us():
    print(app.config['ADMINS'])
    return render_template('home/contact_us.html', title="Contact Us")
