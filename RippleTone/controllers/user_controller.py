from flask import render_template
from views import RegisterForm

# User registration action
@app.route('/register.html', method=['GET', 'POST'])
def signup():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        #create cursor
        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO users(name, email, password) VALUES(%s, %s, %s, %s)", (name, email, password))

        #commit DB
        mysql.connection.commit()

        #close cursor
        cur.close()
        return render_template('register.html')
    return render_template('register.html', form=form)

