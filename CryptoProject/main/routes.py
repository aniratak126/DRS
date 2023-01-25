from flask import render_template, redirect, Blueprint, url_for
from flask_login import current_user

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    '''
    validated = False
    if current_user._get_current_object().validated:
        validated = True
    else:
        validated = False
    return render_template('home.html', validated=validated)
'''
    return render_template('home.html')