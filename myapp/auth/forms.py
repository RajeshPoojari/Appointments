# -*- coding: utf-8 -*-
# external
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms import StringField, PasswordField, RadioField, SubmitField
# internal


class LoginForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired()])
    # email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Parola', validators=[DataRequired()])
    submit = SubmitField('Giriş Yap')


class RegisterForm(FlaskForm):
    fname = StringField('', validators=[DataRequired()])
    lname = StringField('', validators=[DataRequired()])
    email = StringField('', validators=[DataRequired(), Email()])
    username = StringField('', validators=[DataRequired()])
    password = PasswordField('', validators=[DataRequired()])
    password2 = PasswordField('', validators=[DataRequired(),
                                              EqualTo('password')])

    submit = SubmitField('Kaydol')


class ServiceForm(FlaskForm):
    name = StringField('Servis Adı', validators=[DataRequired()])
    price = StringField('Ücreti', validators=[DataRequired()])
    submit = SubmitField('Kaydet', validators=[DataRequired()])
