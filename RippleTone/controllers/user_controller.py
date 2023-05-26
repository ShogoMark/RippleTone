from flask import render_template

# User registration action
def register():
    # Perform registration logic here
    
    # Render the registration template
    return render_template('user/register.html')

# User login action
def login():
    # Perform login logic here
    
    # Render the login template
    return render_template('user/login.html')