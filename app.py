#!/usr/bin/python3

from flask import Flask, render_template, request
from models.user_model import User, RegisterForm, create_user, check_login
from passlib.hash import sha256_crypt
import os
import secrets

app = Flask(__name__)

secret_key = secrets.token_hex(32)
imageFolder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = imageFolder
app.secret_key = secret_key

@app.route('/')
def index():
    image1 = os.path.join(app.config['UPLOAD_FOLDER'], 'first.jpg')
    image2 = os.path.join(app.config['UPLOAD_FOLDER'], 'My project.png')
    return render_template('home.html', user_image = image1, user_image2 = image2)
    return render_template('home.html')

# User registration action
@app.route('/sign_up', methods=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        password = sha256_crypt.encrypt(str(form.password.data))

        create_user(name, password)

    return redirect(url_for('sign_up.html'))
 

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    if request.method == 'POST':
        # Get the username and password entered by the user
        name = request.form.get('name')
        password = request.form.get('password')

        #Perform authentication logic (e.g., check if username and password are valid)
        if check_login(name, password):
            # Authentication successful
            # Redirect the user to a protected page or perform other actions
            return redirect(url_for('dashboard'))
        else:
            # Authentication failed
            error_message = 'Invalid username or password'

    # Render the login template
    return render_template('sign_up.html', error_message=error_message)

if __name__ == '__main__':
    app.run()
