from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

################################################################
# SVI URADITE OVO U TERMINALU DA BI RADILA BAZA KADA POKRENETE
# pip install flask_sqlalchemy
#################################################################
main = Flask(__name__)
login = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
# Initializing the database
db = SQLAlchemy(main)


# Creating db model
class Users(db.Model):
    name = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(15), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String(30), primary_key=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)


# Create a function to return a string when we add someone
def __repr__(self):
    return '<Name %r>' % self.email


@main.route('/')
def index():
    return render_template('home.html')


@main.route('/login')
def logIn():
    return render_template('login.html')


@main.route('/get-name', methods=['POST'])
def get_name():
    name = request.form.get('name')
    return 'Hello, ' + name


@main.route('/register')
def reg():
    return render_template('register.html')


@main.route('/get_user', methods=['GET', 'POST'])
def get_user():
    name_get = request.form.get('name')
    surname_get = request.form.get('surname')
    address_get = request.form.get('address')
    city_get = request.form.get('city')
    country_get = request.form.get('country')
    pnumber_get = request.form.get('pnumber')
    email_get = request.form.get('email')
    password_get = request.form.get('password')

    user = Users(name=name_get, surname=surname_get, address=address_get, city=city_get,
                 country=country_get, phone_number=pnumber_get, email=email_get, password=password_get)
    db.session.add(user)
    db.session.commit()
    return f'Hello, ' + name_get + ' ' + surname_get + ' ' + address_get + ' ' + city_get + ' ' + country_get + ' ' + \
           pnumber_get + ' ' + email_get + ' ' + password_get


def run():
    main.run()
