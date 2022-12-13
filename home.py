from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

################################################################
# SVI URADITE OVO U TERMINALU DA BI RADILA BAZA KADA POKRENETE
# pip install flask_sqlalchemy
#################################################################
main = Flask(__name__)

main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Initializing the database
db = SQLAlchemy(main)

# ovo odkomentarisati samo prvi put kada pokrecete (valjda)
with main.app_context():
    db.create_all()


# Creating db model
class Database(db.Model):
    name = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(15), nullable=False)
    country = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.DateTime, nullable=False, unique=True)
    date = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(30), primary_key=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)


# Create a function to return a string when we add someone
def __repr__(self):
    return '<Name %r>' % self.email


@main.route('/')
def index():
    return render_template('home.html')


@main.route('/register')
def reg():
    return render_template('register.html')


@main.route('/get-name', methods=['POST'])
def get_name():
    name = request.form.get('name')
    return 'Hello, ' + name


def run():
    main.run()
