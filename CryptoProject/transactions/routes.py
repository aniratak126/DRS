from flask import render_template, url_for, flash, redirect, request, Blueprint
from CryptoProject.transactions.forms import TransactionForm
from CryptoProject.models import Transaction, Status, User
from CryptoProject import db
from flask_login import current_user
from random import randint
from Crypto.Hash import keccak
import time, struct

transactions = Blueprint('transactions', __name__)



@transactions.route("/new_transaction", methods=['GET', 'POST'])
def new_transaction():
    form = TransactionForm()
    current_user.money = 1000
    if form.validate_on_submit():
        if current_user.money >= form.amount.data:
            flash('Your transaction is being processed! You will be notified when it has been completed', 'success')
            k = keccak.new(digest_bits=256)
            k.update(bytes(current_user.email, encoding='utf-8') + bytes(form.email.data, encoding='utf-8') + struct.pack("<f", form.amount.data) + bytes(randint(1,99999)))
            transaction_id = k.hexdigest()
            transaction = Transaction(id=transaction_id, sender_id=current_user.email, receiver_id=form.email.data,
                                        amount=form.amount.data, status=Status.IN_PROGRESS.name)

            db.session.add(transaction)
            db.session.commit()

            time.sleep(6)
            user = User.query.filter_by(email=form.email.data).first()
            user.money = user.money + form.amount.data
            transaction_done = Transaction.query.filter_by(id=transaction_id).first()
            transaction_done.status = Status.COMPLETED.name
            db.session.commit()
            flash('Your transaction has been completed!', 'success')

        else:
            k = keccak.new(digest_bits=256)
            k.update(bytes(current_user.email, encoding='utf-8') + bytes(form.email.data, encoding='utf-8') + struct.pack("<f", form.amount.data) + bytes(randint(1, 99999)))
            transaction = Transaction(id=k.hexdigest(), sender_id=current_user.email, receiver_id=form.email.data,
                                      amount=form.amount.data, status=Status.DENIED.name)
            db.session.add(transaction)
            db.session.commit()
            flash('Insufficient funds!', 'danger')
    return render_template('transaction.html', form=form)


