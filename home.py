from flask import Flask, render_template, request
main = Flask(__name__)

@main.route('/')
def index():
    return render_template('home.html')


@main.route('/get-name', methods=['POST'])
def get_name():
    name = request.form.get('name')
    return 'Hello, ' + name

def run():
    main.run()
