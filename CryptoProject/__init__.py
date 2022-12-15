from flask import Flask
from flask_sqlalchemy import SQLAlchemy
################################################################
# SVI URADITE OVO U TERMINALU DA BI RADILA BAZA KADA POKRENETE
# pip install flask_sqlalchemy
#################################################################
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Initializing the database
db = SQLAlchemy(app)

from CryptoProject import routes
# NE PENJI OVAJ IMPORT SKROZ GORE !!!!!!!!!!
