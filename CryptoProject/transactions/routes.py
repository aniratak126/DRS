from flask import render_template, url_for, flash, redirect, request, Blueprint

transactions = Blueprint('transactions', __name__)


@transactions.route("/new_transaction")
def new_transaction():
    
    return redirect(url_for('main.home'))
