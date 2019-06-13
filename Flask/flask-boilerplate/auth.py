from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from forms import LoginForm, RegisterForm, ForgotForm
from app import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return str({
            email,
            password,
        })
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        error = None
        if not name:
            error = "Name is required"
        if not email:
            error = "Email is required"
        if not password:
            error = "Password is Required"
        elif (User.query.filter_by(email=email).first()
        ) is not None:
            error = 'User {} already exists'.format(name, )
        if error is None:
            new_user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        flash(error)
        return redirect(request.url)

    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@auth.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)


@auth.route('/logout')
def logout():
    return 'Logout'
