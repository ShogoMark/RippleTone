#!/usr/bin/python3

import uuid
from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/RippleApp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/RippleApp')

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()

class RegisterForm(FlaskForm):
    firstname = StringField('firstname', validators=[DataRequired()])
    lastname = StringField('lastname', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(36), unique=True, default=str(uuid.uuid4()))
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
    # Create a session
    session = Session()
    
    # Query the user by username
    user = session.query(User).filter(User.username == username).first()
    
    if user is None:
        return False  # User not found
    
    if user.password == password:
        return True  # Login successful
    
    return False  # Incorrect password


def create_user(firstname, lastname, username, password, country, email):
    # Create a session
    session = Session()

    # Create a new User instance
    user = User(firstname=firstname, lastname=lastname, username=username, password=password, country=country, email=email)

    # Add the user to the session
    session.add(user)

    # Commit the session to save the changes to the database
    session.commit()

    # Close the session
    session.close()

if __name__ == '__main__':
    app.run()
