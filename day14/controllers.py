from app import app
from flask import render_template, request, redirect, url_for
from forms import RegisterForm, LoginForm
from models import User
from werkzeug.security import generate_password_hash
from flask_login import login_user, login_required



@app.route('/layout')
@login_required
def layouts():
    return render_template('layout.html')



@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if request.method == 'POST':
        print('post')
        form = RegisterForm(request.form)
        print(request.form)
        if form.validate_on_submit():
            print('valid')
            user = User(
                name = form.name.data,
                email = form.email.data,
                password = generate_password_hash(form.password.data)
            )
            user.save()
        return redirect(url_for('login_page'))
    return render_template('login.html', form=form)





@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.form)
        print('valid')
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            print('login')
            return redirect(url_for('layouts'))
    return render_template('sign.html', form = form)


