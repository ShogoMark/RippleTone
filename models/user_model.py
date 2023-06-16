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
    Firstname = StringField('Firstname', validators=[DataRequired()])
    Lastname = StringField('Lastname', validators=[DataRequired()])
    Username = StringField('Username', validators=[DataRequired()])
    Password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
    submit = SubmitField('Sign Up')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(36), unique=True, default=str(uuid.uuid4()))
    Username = Column(String(100), unique=True)
    Password = Column(String(100))
    Country = Column(String(100))
    Email = Column(String(100))

    def __init__(self, Firstname, Lastname, Username, Password, Country, Email):
        self.user_id = str(uuid.uuid4())
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Username = Username
        self.Password = Password
        self.Country = Country
        self.Email = Email

class LoginForm(FlaskForm):
    Username = StringField('Username', validators=[DataRequired()])
    Password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

# Function to check login details
def check_login(Username, Password):
    # Create a session
    session = Session()
    
    # Query the user by username
    user = session.query(User).filter(User.Username == Username).first()
    
    if user is None:
        return False  # User not found
    
    if user.Password == Password:
        return True  # Login successful
    
    return False  # Incorrect password


def create_user(Firstname, Lastname, Username, Password, Country, Email):
    # Create a session
    session = Session()

    # Create a new User instance
    user = User(Firstname=Firstname, Lastname=Lastname, Username=Username, Password=Password, Country=Country, Email=Email)

    # Add the user to the session
    session.add(user)

    # Commit the session to save the changes to the database
    session.commit()

    # Close the session
    session.close()

if __name__ == '__main__':
    app.run()
