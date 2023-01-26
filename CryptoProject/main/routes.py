from flask import render_template, redirect, Blueprint, url_for
from flask_login import current_user
import json
import requests

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    # defining key/request url
    key = "https://api.binance.com/api/v3/ticker/price?symbol="
    currencies = ["BTCUSDT", "DOGEUSDT", "LTCUSDT","XRPUSDT", "ETHUSDT"]
    j = 0
    cryptos = dict()
    # requesting data from url
    for i in currencies:
        # completing API for request
        url = key + currencies[j]
        data = requests.get(url)
        data = data.json()
        j = j + 1
        coin = f"\n{data['symbol']} price is {data['price']}"
        if data['symbol'] == "BTCUSDT":
            currency = "Bitcoin"
        elif data['symbol'] == "DOGEUSDT":
            currency = "Dogecoin"
        elif data['symbol'] == "LTCUSDT":
            currency = "Litecoin"
        elif data['symbol'] == "XRPUSDT":
            currency = "Ripple"
        elif data['symbol'] == "ETHUSDT":
            currency = "Ethereum"
        cryptos[currency] = data["price"]


    # ovde pravi gresku
    if not current_user.is_anonymous:
        if current_user._get_current_object().validated:
            return redirect(url_for('users.logged'))
        else:
            return redirect(url_for('users.verification'))
    return render_template('home.html', title='Home', cryptos=cryptos)



''' 
ako bude pravilo problema ovo gore 
UPDATE: pravi problem - vraca na login umesto home

def home():
    if current_user.is_anonymous:
        return redirect(url_for('users.login'))
    else:
        if current_user._get_current_object().validated:
            return redirect(url_for('users.logged'))
        else:
            return redirect(url_for('users.verification'))
    return render_template('home.html', validated=validated)
'''
