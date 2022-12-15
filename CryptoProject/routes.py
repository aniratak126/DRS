from flask import render_template, request
from CryptoProject import app, db
from CryptoProject.models import Users


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login_user', methods=['GET', 'POST'])
def login_user():
    # TO DO
    return 'successfully'


@app.route('/get-name', methods=['POST'])
def get_name():
    name = request.form.get('name')
    return 'Hello, ' + name


@app.route('/register')
def reg():
    return render_template('register.html')


@app.route('/get_user', methods=['GET', 'POST'])
def get_user():
    name_get = request.form.get('name')
    surname_get = request.form.get('surname')
    address_get = request.form.get('address')
    city_get = request.form.get('city')
    country_get = request.form.get('country')
    phone_number_get = request.form.get('phone_number')
    email_get = request.form.get('email')
    password_get = request.form.get('password')

    user = Users(name=name_get, surname=surname_get, address=address_get, city=city_get,
                 country=country_get, phone_number=phone_number_get, email=email_get, password=password_get)
    db.session.add(user)
    db.session.commit()
    return f'Hello, ' + name_get + ' ' + surname_get + ' ' + address_get + ' ' + city_get + ' ' + country_get + ' ' + \
           phone_number_get + ' ' + email_get + ' ' + password_get
