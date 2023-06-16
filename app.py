#!/usr/bin/python3

from flask import Flask, render_template, request, redirect
from models.user_model import User, LoginForm, RegisterForm, create_user, check_login
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
        Firstname = form.Firstname.data
        Lastname = form.Lastname.data
        Username = form.Username.data
        Country = form.Country.data
        Email = form.Email.data
        Password = sha256_crypt.encrypt(str(form.Password.data))
        confirm_password = form.confirm_password.data

        #validating the password and confirm password
        if Password != confirm_password:
            return redirect(url_for('home.html'))

    return render_template('sign_up.html', error='Passwords do not match', form=form)


    create_user(Firstname, Lastname, Username, Password, Country, Email)
 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        Username = form.username.data
        Password = form.password.data

		#Perform authentication logic (e.g., check if username and password are valid)
        if check_login(Username, Password):
            # Authentication successful
            # Redirect the user to a protected page or perform other actions
            return redirect(url_for('dashboard'))
    # Render the login template
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
