# -*- coding: utf-8 -*-
# external
from threading import Thread
from datetime import datetime
# To send email
from itsdangerous import SignatureExpired, URLSafeTimedSerializer
from flask import render_template
from flask_mail import Message

# internal
from myapp import mail, app


def generate_token(email):
    """generates token for given email"""
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])


def verify_token(token, expiration=3600):
    """ returns email, """
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(token,
                                 salt=app.config['SECURITY_PASSWORD_SALT'],
                                 max_age=expiration)
    except SignatureExpired:
        return "<h1>Time expired</h1>"
    return email


def send_async_email(app, msg):
    """sends asynchronous mail"""
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email,
           args=(app, msg)).start()


def send_confirmation_token(client):
    """ sends email with token"""
    token = generate_token(client.email)
    subject = "Email Doğrulama"
    send_email(
        subject,
        sender=app.config['ADMINS'][0],
        recipients=[client.email],
        text_body=render_template(
            'email/confirm_email.txt', token=token, client=client),
        html_body=render_template(
            'email/confirm_email.html', token=token, client=client)
    )


def send_bill_mail(client, booking):
    subject = "Fatura"
    send_email(
        subject,
        sender=app.config['ADMINS'][0],
        recipients=[client.email],
        text_body=render_template('email/bill.txt', booking=booking),
        html_body=render_template('email/bill.html', booking=booking),
    )


def convert_to_datetime(date, time):
    """ converts given string date and time to datetime """
    lidate = date.split('.')
    litime = time.split('.')
    lidate.extend(litime)
    lidate = [int(i[1]) if i[0] == "0" else int(i) for i in lidate]
    return datetime(lidate[0], lidate[1], lidate[2], lidate[3], lidate[4])
