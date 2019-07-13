# -*- coding: utf-8 -*-
# external
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms import StringField, PasswordField, RadioField, SubmitField
# internal


class LoginForm(FlaskForm):
    username = StringField('User name', validators=[DataRequired()])
    # email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign in')


class RegisterForm(FlaskForm):
    fname = StringField('', validators=[DataRequired()])
    lname = StringField('', validators=[DataRequired()])
    email = StringField('', validators=[DataRequired(), Email()])
    username = StringField('', validators=[DataRequired()])
    password = PasswordField('', validators=[DataRequired()])
    password2 = PasswordField('', validators=[DataRequired(),
                                              EqualTo('password')])

    submit = SubmitField('Register')


class ServiceForm(FlaskForm):
    name = StringField('Service Name', validators=[DataRequired()])
    price = StringField('Fare', validators=[DataRequired()])
    submit = SubmitField('Save', validators=[DataRequired()])
