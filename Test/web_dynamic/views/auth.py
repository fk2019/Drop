#!/usr/bin/python3
"""auth blueprint"""
from flask import Blueprint, render_template, request, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from models import storage

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = storage._DBStorage__session.query(User).filter_by(user_name=username).first()
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
    return redirect(url_for('main.profile'))


@auth.route('/register')
def register_user():
    return render_template('register.html')


@auth.route('/register', methods=['POST'])
def register_user_post():
    email = request.form.get('email')
    password = request.form.get('password')
    password = generate_password_hash(password, method='sha256')
    user_name = request.form.get('user_name')
    args = {'email': email, 'password': password, 'user_name': user_name}
    us2 = storage._DBStorage__session.query(User).filter_by(
        email=email).first()
    if us2:
        flash('Email already exists!')
        return render_template('register.html')
    user = User(**args)
    user.save()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    return render_template('logout.html')
