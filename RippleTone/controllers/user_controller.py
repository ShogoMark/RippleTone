#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
from views import RegisterForm
from passlib.hash import sha256_crypt
from models import create_user, check_login

app = Flask(__name__)

# User registration action
@app.route('/register.html', methods=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.name.data
        password = sha256_crypt.encrypt(str(form.password.data))

        create_user(username, password)

        return redirect(url_for('index'))
 

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        # Get the username and password entered by the user
        username = request.form.get('username')
        password = request.form.get('password')

        # Perform authentication logic (e.g., check if username and password are valid)
        if check_login(username, password):
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