#!/usr/bin/python3

from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/RippleApp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/RippleApp')

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(36), unique=True, default=str(uuid.uuid4()))
    name = Column(String(100), unique=True)
    password = Column(String(100))

    def __init__(self, name, password):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.password = password
        self.preferences = {}
        self.history = []

    def add_preference(self, item_id, rating):
        self.preferences[item_id] = rating

    def add_to_history(self, item_id):
        self.history.append(item_id)

# Function to check login details
def check_login(name, password):
    # Create a session
    session = Session()
    
    # Query the user by username
    user = session.query(User).filter(User.username == username).first()
    
    if user is None:
        return False  # User not found
    
    if user.password == password:
        return True  # Login successful
    
    return False  # Incorrect password


def create_user(name, password):
    # Create a session
    session = Session()

    # Create a new User instance
    user = User(name=name, email=email, password=password)

    # Add the user to the session
    session.add(user)

    # Commit the session to save the changes to the database
    session.commit()

    # Close the session
    session.close()

if __name__ == '__main__':
    app.run()