from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TelField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from CryptoProject.models import User


class TransactionForm(FlaskForm):
    email = StringField('Email of the person u wish to transfer the funds to',
                        validators=[DataRequired(), Email()])
    amount = FloatField('Amount u wish to transfer',
                        validators=[DataRequired()])
    submit = SubmitField('Transfer')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('That user doesn\'t exist. Please check the spelling or choose a different one.')
        elif user.email == current_user._get_current_object().email:
            raise ValidationError('You can\'t deposit to your own account!')
        elif not user.validated:
            raise ValidationError('The user account you have selected is not activated')

    def validate_amount(self, amount):
        if amount.data < 0.0:
            raise ValidationError('Amount you wish to transfer canno\'t be lower than 0!')


class DepositForm(FlaskForm):
    amount = FloatField('Amount u wish to deposit into your account', validators=[DataRequired()])

    submit = SubmitField('Deposit')

    def validate_amount(self, amount):
        if amount.data < 0.0:
            raise ValidationError('Amount you wish to deposit canno\'t be lower than 0!')
