from flask import render_template, redirect, Blueprint, url_for
from flask_login import current_user

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    # ovde pravi gresku
    validated=False

    if current_user.is_anonymous:
        return redirect(url_for('users.login'))
    else:
        if current_user._get_current_object().validated:
            return redirect(url_for('users.logged'))
        else:
            validated = False

    return render_template('home.html', validated=validated)