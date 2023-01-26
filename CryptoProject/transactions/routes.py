from flask import render_template, url_for, flash, redirect, request, Blueprint
from CryptoProject.transactions.forms import TransactionForm
from CryptoProject.models import Transaction, Status
from CryptoProject import db
from flask_login import current_user
from random import randint
from Crypto.Hash import keccak

transactions = Blueprint('transactions', __name__)


@transactions.route("/new_transaction")
def new_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        k = keccak.new(digest_bits=256)
        k.update(bytes(current_user.email) + bytes(form.email.data) + bytes(form.amount.data) + bytes(randint(1,99999)))
        transaction = Transaction(id=k.hexdigest(), sender_id=current_user.email, receiver_id=form.email.data,
                                  amount=form.amount.data, status=Status.IN_PROGRESS.name)
        db.session.add(transaction)
        db.session.commit()
    return redirect(url_for('main.home'))

