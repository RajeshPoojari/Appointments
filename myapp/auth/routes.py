# -*- coding: utf-8 -*-
# external
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from datetime import datetime

# internal
from myapp.auth import bp
from myapp.auth.forms import LoginForm, RegisterForm, ServiceForm
from myapp.auth.models import User, Booking
from myapp.home.models import Service
from myapp import db


@bp.route('/dashboard')
@login_required
def dashboard():
    bookings = Booking.query.filter(Booking.activated == True).all()
    return render_template('auth/dashboard.html', title="Yönetici Anasayfa", bookings=bookings)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Kullanıcı adı veya parola hatalı', 'danger')
            return redirect(url_for('auth.login'))
        login_user(user)
        flash("Sisteme giriş yaptınız.")
        return redirect(url_for('auth.dashboard'))
    return render_template('auth/login.html', title="Giriş yap", form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@bp.route('/register', methods=['GET', 'POST'])
@login_required
def register():
    if current_user.is_admin:
        form = RegisterForm()
        if form.validate_on_submit():
            fname = form.fname.data
            lname = form.lname.data
            email = form.email.data
            username = form.username.data
            user = User(fname=fname, lname=lname,
                        email=email, username=username)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash("Yeni kullanıcı başarıyla kaydedildi", "success")
            return redirect(url_for('auth.register'))
        return render_template('auth/register.html', title='Kaydol', form=form)
    else:
        return render_template('errors/403.html'), 403


@bp.route('/add_service', methods=['GET', 'POST'])
@login_required
def add_service():
    if current_user.is_admin:
        form = ServiceForm()
        services = Service.query.all()
        if form.validate_on_submit():
            service = Service(name=form.name.data, price=form.price.data)
            db.session.add(service)
            db.session.commit()
            flash('Servis eklendi', 'success')
            return redirect(url_for('auth.add_service'))
        return render_template('auth/service_form.html',
                               title='Servis Ekle',
                               form=form, services=services)
    else:
        return render_template('errors/403.html'), 403
