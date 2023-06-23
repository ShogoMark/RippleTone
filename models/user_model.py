#!/usr/bin/python3

import uuid
from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_sqlalchemy import SQLAlchemy
from store import user_data, save_user_data
from passlib.hash import sha256_crypt

app = Flask(__name__)


class RegisterForm(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class User():
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(36), unique=True, default=str(uuid.uuid4))
    username = Column(String(100), unique=True)
    password = Column(String(100))
    country = Column(String(100))
    email = Column(String(100))

    def __init__(self, firstname, lastname, username, password, country, email):
        self.user_id = str(uuid.uuid4())
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.country = country
        self.email = email

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Log In')

# Function to check login details
def check_login(username, password):
    if username in user_data:
        user = user_data[username]
        stored_password = user['password']
        if sha256_crypt.verify(password, stored_password):
            return True
    return False


def create_user(firstname, lastname, username, password, country, email):
    user = {
        'firstname': firstname,
        'lastname': lastname,
        'username': username,
        'password': password,
        'country': country,
        'email': email
    }

    user_data[username] = user
    save_user_data(user_data)



if __name__ == '__main__':
    app.run()
