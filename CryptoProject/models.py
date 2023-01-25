from datetime import datetime, timezone, timedelta
from flask import current_app
from CryptoProject import db, login_manager
from flask_login import UserMixin
import jwt


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# NOVA KLASA USER
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(25), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    city = db.Column(db.String(25), nullable=False)
    state = db.Column(db.String(25), nullable=False)
    cellphone = db.Column(db.Integer, unique=True, nullable=False)

    def get_reset_token(self, expired_sec=1800):
        s = jwt.encode({"exp": datetime.now(tz=timezone.utc) + timedelta(
            seconds=expired_sec), "user_id": self.id}, current_app.config['SECRET_KEY'], algorithm="HS256")
        return s

    @staticmethod
    def verify_reset_token(token):
        try:
            s = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            user_id = s['user_id']
        except:
            return None
        return User.query.get(user_id)


'''
NEPOTREBNO
class Post(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
'''
