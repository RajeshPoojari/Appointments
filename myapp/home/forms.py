# -*- coding: utf-8 -*-
# external
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms import StringField, SubmitField
# internal


class BookingForm(FlaskForm):
    fname = StringField('', validators=[DataRequired()])
    lname = StringField('', validators=[DataRequired()])
    phone = StringField('', validators=[DataRequired()])
    email = StringField('', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')