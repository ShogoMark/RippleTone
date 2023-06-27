#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, url_for
from models.user_model import User, LoginForm, RegisterForm, create_user, check_login
from passlib.hash import sha256_crypt
import os
import secrets
from sqlalchemy import create_engine, Column, String, Integer
from store import user_data
from flask import jsonify
import json

app = Flask(__name__)

secret_key = secrets.token_hex(32)
imageFolder = os.path.join('static', 'images')

app.config['UPLOAD_FOLDER'] = imageFolder
app.secret_key = secret_key


@app.route('/')
def index():
        image1 = os.path.join(app.config['UPLOAD_FOLDER'], 'hamburger.svg')
        image2 = os.path.join(app.config['UPLOAD_FOLDER'], 'My project.png')
        image3 = os.path.join(app.config['UPLOAD_FOLDER'], 'image-671.png')
        image4 = os.path.join(app.config['UPLOAD_FOLDER'], 'th.jpg')
        image5 = os.path.join(app.config['UPLOAD_FOLDER'], 'third.jpg')
        image6 = os.path.join(app.config['UPLOAD_FOLDER'], 'college.jpg')
        image7 = os.path.join(app.config['UPLOAD_FOLDER'], 'icon-close.svg')
        return render_template('landingpage.html', user_image = image1, user_image2 = image2, user_image3 = image3, user_image4 = image4, user_image5 = image5, user_image6 = image6, user_image7 = image7)
        return render_template('landingpage.html')


@app.route('/home')
def home():
    image1 = os.path.join(app.config['UPLOAD_FOLDER'], 'first.jpg')
    image2 = os.path.join(app.config['UPLOAD_FOLDER'], 'My project.png')
    return render_template('home.html', user_image = image1, user_image2 = image2)
    return render_template('home.html')

# User registration action
@app.route('/sign_up', methods=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        username = form.username.data
        country = form.country.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))
        confirm_password = form.confirm_password.data

        #validating the password and confirm password
        if password != confirm_password:
            return render_template('sign_up.html', error='Passwords do not match', form=form)

        create_user(firstname, lastname, username, password, country, email)


        return redirect(url_for('success'))

    return render_template('sign_up.html', form=form)

@app.route('/success')
def success():
    return "User registered successfully!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

		#Perform authentication logic (e.g., check if username and password are valid)
        if check_login(username, password):
            # Authentication successful
            # Redirect the user to a protected page or perform other actions
            return redirect(url_for('dashboard'))
    # Render the login template
    return render_template('login.html', form=form)

@app.route('/user_data')
def display_user_data():
    try:
        with open('user_data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return "No user data found."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
