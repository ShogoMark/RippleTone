#!/usr/bin/python3

from flask import Flask, render_template
from models.user_model import User, RegisterForm, create_user, check_login
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# User registration action
@app.route('/sign_up', methods=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        password = sha256_crypt.encrypt(str(form.password.data))

        create_user(name, password)

    return redirect(url_for('index')
 

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        # Get the username and password entered by the user
        name = request.form.get('name')
        password = request.form.get('password')

         Perform authentication logic (e.g., check if username and password are valid)
        if check_login(name, password):
            # Authentication successful
            # Redirect the user to a protected page or perform other actions
            return redirect(url_for('dashboard'))
        else:
            # Authentication failed
            error_message = 'Invalid username or password'

    # Render the login template
    return render_template('user/login.html', error_message=error_message)

if __name__ == '__main__':
    app.run()
