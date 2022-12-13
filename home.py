from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from mysql import connector

# SVI URADITE OVO U TERMINALU DA BI RADILA BAZA KADA POKRENETE
# pip install mysqlclient
# pip install mysql-python

# AKO I DALJE NE RADI IDITE REDOM I DODAJTE JEDAN PO JEDAN DOK NE PRORADI
# mysql-connector
# mysql-connector-python
# mysql-connector-python-rf


main = Flask(__name__)

main.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/users'
# Initializing the database
db = SQLAlchemy(main)

# dodaj ovde db.create_all()


# Creating db model
class Database(db.Model):
    name = db.Column(db.String(15), nullable=False)
    surname = db.Column(db.String(15), nullable=False)
    date = db.Column(db.DateTime)
    email = db.Column(db.Email, primary_key=True)


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
