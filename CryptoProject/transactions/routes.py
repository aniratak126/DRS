from flask import render_template, url_for, flash, redirect, request, Blueprint
from CryptoProject.transactions.forms import TransactionForm
from CryptoProject.models import Transaction, Status, User
from CryptoProject import db
from flask_login import current_user
from random import randint
from Crypto.Hash import keccak
import time

transactions = Blueprint('transactions', __name__)



@transactions.route("/new_transaction", methods=['GET', 'POST'])
def new_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        if current_user.money >= form.amount.data:
            k = keccak.new(digest_bits=256)
            k.update(bytes(current_user.email) + bytes(form.email.data) + bytes(form.amount.data) + bytes(randint(1,99999)))
            transaction = Transaction(id=k.hexdigest(), sender_id=current_user.email, receiver_id=form.email.data,
                                        amount=form.amount.data, status=Status.IN_PROGRESS.name)
            db.session.add(transaction)
            db.session.commit()
            flash('Your transaction is being processed! You will be notified when it has been completed', 'success')
            time.sleep(100)
            user = User.query.filter_by(email=form.email.data).first()
            user.money = user.money + form.amount.data
            user.state = Status.COMPLETED.name
            db.session.commit()
            flash('Your transaction has been completed!', 'success')

        else:
            k = keccak.new(digest_bits=256)
            k.update(bytes(current_user.email) + bytes(form.email.data) + bytes(form.amount.data) + bytes(randint(1, 99999)))
            transaction = Transaction(id=k.hexdigest(), sender_id=current_user.email, receiver_id=form.email.data,
                                      amount=form.amount.data, status=Status.DENIED.name)
            db.session.add(transaction)
            db.session.commit()
            flash('Insufficient funds!', 'danger')
    return redirect(url_for('transactions.transaction'))



