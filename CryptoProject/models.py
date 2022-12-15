from CryptoProject import db


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
