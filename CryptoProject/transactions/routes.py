import struct
import threading
import time
from random import randint
from Crypto.Hash import keccak
from flask import render_template, flash, Blueprint, redirect, url_for
from flask_login import current_user, login_required
from CryptoProject import db
from CryptoProject.models import Transaction, Status, User
from CryptoProject.transactions.forms import TransactionForm, DepositForm

transactions = Blueprint('transactions', __name__)


@transactions.route("/new_transaction", methods=['GET', 'POST'])
@login_required
def new_transaction():
    if not current_user._get_current_object().validated:
        flash('Your account is not activated for you to be able to make a transaction!', 'danger')
        return redirect(url_for('users.verification'))
    form = TransactionForm()
    if form.validate_on_submit():
        if form.currency.data == 'money':
            helpvar = current_user.money
            helpvar2 = 'money'
        elif form.currency.data == 'bitcoin':
            helpvar = current_user.bitcoin
            helpvar2 = 'bitcoin'
        elif form.currency.data == 'dogecoin':
            helpvar = current_user.dogecoin
            helpvar2 = 'dogecoin'
        elif form.currency.data == 'litecoin':
            helpvar = current_user.litecoin
            helpvar2 = 'litecoin'
        elif form.currency.data == 'ripple':
            helpvar = current_user.ripple
            helpvar2 = 'ripple'
        else:
            helpvar = current_user.ethereum
            helpvar2 = 'ethereum'

        if helpvar >= form.amount.data:
            flash('Your transaction is being processed! After 5 minutes check your Transaction History'
                  ' for information about your transaction', 'success')
            k = keccak.new(digest_bits=256)
            k.update(
                bytes(current_user.email, encoding='utf-8') + bytes(form.email.data, encoding='utf-8') + struct.pack(
                    "<f", form.amount.data) + bytes(randint(1, 99999)))
            transaction_id = k.hexdigest()
            transaction = Transaction(id=transaction_id, sender_id=current_user.email, receiver_id=form.email.data,
                                      amount=form.amount.data, status=Status.IN_PROGRESS.name, currency=helpvar)
            db.session.add(transaction)
            db.session.commit()
            sender = current_user.email
            try:
                threading.Thread(target=transaction_thread, args=(form.email.data, form.amount.data,
                                                                  transaction_id, sender, helpvar2)).start()
            finally:
                return redirect(url_for('users.logged'))
        else:
            k = keccak.new(digest_bits=256)
            k.update(
                bytes(current_user.email, encoding='utf-8') + bytes(form.email.data, encoding='utf-8') + struct.pack(
                    "<f", form.amount.data) + bytes(randint(1, 99999)))
            transaction = Transaction(id=k.hexdigest(), sender_id=current_user.email, receiver_id=form.email.data,
                                      amount=form.amount.data, status=Status.DENIED.name, currency=helpvar)
            db.session.add(transaction)
            db.session.commit()
            flash('Insufficient funds!', 'danger')
    return render_template('transaction.html', form=form, verified=True)


@transactions.route("/deposit", methods=['GET', 'POST'])
@login_required
def deposit():
    if not current_user._get_current_object().validated:
        flash('Your account is not activated', 'danger')
        return redirect(url_for('users.verification'))
    form = DepositForm()
    if form.validate_on_submit():
        try:
            current_user.money = current_user.money + form.amount.data
            db.session.commit()
            flash('Your transaction has been processed.'
                  f' The amount of {form.amount.data} has been added to your personal account', 'success')
        except:
            flash('Your transaction has been denied', 'danger')
    return render_template('deposit.html', form=form, verified=True)


@transactions.route("/history")
@login_required
def transaction_history():
    if not current_user._get_current_object().validated:
        flash('Your account is not activated', 'danger')
        return redirect(url_for('users.verification'))
    historySend = Transaction.query.filter_by(sender_id=current_user.email).all()
    historyRecv = Transaction.query.filter_by(receiver_id=current_user.email).all()
    return render_template('history.html', historySend=historySend, historyRecv=historyRecv, verified=True)


def transaction_thread(email, amount, transaction_id, sender, helpvar):
    from run import app
    time.sleep(2)
    try:
        with app.app_context():
            user = User.query.filter_by(email=email).first()
            i_did_it = User.query.filter_by(email=sender).first()
            transaction_done = Transaction.query.filter_by(id=transaction_id).first()
            if helpvar == 'money':
                if i_did_it.money - amount < 0:
                    transaction_done.status = Status.DENIED.name
                    transaction_done.currency = 'dollar'
                else:
                    user.money = user.money + amount
                    i_did_it.money = i_did_it.money - amount
                    transaction_done.status = Status.COMPLETED.name
                    transaction_done.currency = helpvar
            elif helpvar == 'bitcoin':
                if i_did_it.bitcoin - amount < 0:
                    transaction_done.status = Status.DENIED.name
                    transaction_done.currency = helpvar
                else:
                    user.bitcoin = user.bitcoin + amount
                    i_did_it.bitcoin = i_did_it.bitcoin - amount
                    transaction_done.status = Status.COMPLETED.name
                    transaction_done.currency = helpvar
            elif helpvar == 'dogecoin':
                if i_did_it.dogecoin - amount < 0:
                    transaction_done.status = Status.DENIED.name
                    transaction_done.currency = helpvar
                else:
                    user.dogecoin = user.dogecoin + amount
                    i_did_it.dogecoin = i_did_it.dogecoin - amount
                    transaction_done.status = Status.COMPLETED.name
                    transaction_done.currency = helpvar
            elif helpvar == 'litecoin':
                if i_did_it.litecoin - amount < 0:
                    transaction_done.status = Status.DENIED.name
                    transaction_done.currency = helpvar
                else:
                    user.litecoin = user.litecoin + amount
                    i_did_it.litecoin = i_did_it.litecoin - amount
                    transaction_done.status = Status.COMPLETED.name
                    transaction_done.currency = helpvar
            elif helpvar == 'ripple':
                if i_did_it.ripple - amount < 0:
                    transaction_done.status = Status.DENIED.name
                    transaction_done.currency = helpvar
                else:
                    user.ripple = user.ripple + amount
                    i_did_it.ripple = i_did_it.ripple - amount
                    transaction_done.status = Status.COMPLETED.name
                    transaction_done.currency = helpvar
            elif helpvar == 'ethereum':
                if i_did_it.ethereum - amount < 0:
                    transaction_done.status = Status.DENIED.name
                    transaction_done.currency = helpvar
                else:
                    user.ethereum = user.ethereum + amount
                    i_did_it.ethereum = i_did_it.ethereum - amount
                    transaction_done.status = Status.COMPLETED.name
                    transaction_done.currency = helpvar
            db.session.commit()
    except:
        with app.app_context():
            transaction_done = Transaction.query.filter_by(id=transaction_id).first()
            transaction_done.status = Status.DENIED.name
            transaction_done.currency = helpvar
            db.session.commit()
