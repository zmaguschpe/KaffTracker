from flask import Blueprint, render_template, request, redirect, url_for
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db 
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/', methods=['GET', 'POST'])
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return render_template("cu.html", user=current_user)
            else:
                return '<p>Incorrect password</p>'
        else:
            return '<p>Username does not exist</p>'

    return render_template("login.html", user=current_user)

@auth.route('/profile')
def showuser():
    return render_template("cu.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            return 'username already taken'        
        elif len(username) < 2:
            return'username must be greater than 1 character'
        elif len(password) < 2:
            return'Password must be at least 2 characters.'
        else:
            new_user = User(username=username, password=generate_password_hash(
                password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            print('Account created')
            return redirect(url_for('auth.login'))
    return render_template("register.html")
