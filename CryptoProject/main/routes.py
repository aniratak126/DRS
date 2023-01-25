from flask import render_template, redirect, Blueprint, url_for
from flask_login import current_user

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    if current_user:
        if current_user._get_current_object().validated:
            return render_template('home.html')
        else:
            return redirect(url_for('users.verification'))
    else:
        return render_template('home.html')