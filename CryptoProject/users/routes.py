from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from CryptoProject import db, bcrypt
from CryptoProject.models import User
from CryptoProject.users.forms import (RegistrationForm, LoginForm, UpdateAccountForm, VerificationForm)

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user:
        loged = True
    else:
        loged = False
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, name=form.name.data, surname=form.surname.data, address=form.address.data, city=form.city.data, state=form.state.data, cellphone=form.cellphone.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form, loged=loged)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user:
        loged = True
    else:
        loged = False
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form, loged=loged)


@users.route("/logout")
def logout():
    if current_user:
        loged = True
    else:
        loged = False
    logout_user()
    return redirect(url_for('main.home', loged=loged))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    if current_user:
        loged = True
    else:
        loged = False
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.name = form.name.data
        current_user.surname = form.surname.data
        current_user.address = form.address.data
        current_user.city = form.city.data
        current_user.state = form.state.data
        current_user.cellphone = form.cellphone.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.name.data = current_user.name
        form.surname.data = current_user.surname
        form.address.data = current_user.address
        form.city.data = current_user.city
        form.state.data = current_user.state
        form.cellphone.data = current_user.cellphone
    return render_template('account.html', title='Account', form=form, loged=loged)


@users.route("/verification", methods=['GET', 'POST'])
@login_required
def verification():
    form = VerificationForm()
    if current_user:
        loged = True
    else:
        loged = False

    #Ovde sad da se proveri za karticu i da se vrati stranica koja treba
    return render_template('verification.html', title='Verification', form=form, loged=loged)