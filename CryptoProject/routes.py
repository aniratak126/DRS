from flask import render_template, request, redirect, url_for
from CryptoProject import app, db
from CryptoProject.models import Users


@app.route('/')
def index():
    return redirect(url_for('home'))


@app.route('/logged')
def logged():
    return render_template('loggeduser.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login_user', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()
        if user:
            if user.password == password:
                return redirect(url_for('logged'))
            else:
                return f'Wrong password'
        else:
            return f'User with email: '+email+' does not exist.'

    return 'success'


@app.route('/get-name', methods=['POST'])
def get_name():
    name = request.form.get('name')
    return 'Hello, ' + name


@app.route('/register')
def reg():
    return render_template('register.html')


@app.route('/get_user', methods=['GET', 'POST'])
def get_user():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        address = request.form.get('address')
        city = request.form.get('city')
        country = request.form.get('country')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        password = request.form.get('password')

        user = Users.query.filter_by(email=email).first()

        if user:
            return f'User with that email already exist.'
        elif len(email) < 4:
            return f'Email must be greater than 3 characters.'
        elif len(password) < 7:
            return f'Password must be greater than 7 characters.'
        else:
            new_user = Users(name=name, surname=surname, address=address, city=city, country=country,
                             phone_number=phone_number, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return 'success'
    return 'success'
