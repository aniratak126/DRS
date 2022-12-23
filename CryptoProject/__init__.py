from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.secret_key = 'BAD_SECRET_KEY'
# Initializing the database
db = SQLAlchemy(app)

# NE PENJI OVAJ IMPORT SKROZ GORE !!!!!!!!!!
from CryptoProject import routes
# NE PENJI OVAJ IMPORT SKROZ GORE !!!!!!!!!!
