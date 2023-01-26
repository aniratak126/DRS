from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TelField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from CryptoProject.models import User



class TransactionForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    amount = FloatField('Amount',
                        validators=[DataRequired()])
    submit = SubmitField('Transfer')