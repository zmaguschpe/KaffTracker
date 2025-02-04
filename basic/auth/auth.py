from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db 
from flask_login import login_user, login_required, logout_user, current_user
from .forms import LoginForm, RegisterForm

auth = Blueprint('auth', __name__, template_folder='templates')

@auth.route('/', methods=['GET', 'POST'])
@auth.route('/login', methods=['GET', 'POST'])
def login():
# if current_user not loged in
    form = LoginForm()
    if request.method == 'POST'and form.validate_on_submit():
        #sinn??
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first() #first_or_404(), one 
     
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)

                #return redirect(url_for('.profile'))
                return redirect(request.args.get("next") or url_for(".profile"))
            #funzt nicht
            
            else:
                flash("wrong password") # Styling, "error"s
                return redirect(url_for('auth.login'))
        else:
            flash("Username does not exist") #, "error"s
            return redirect(url_for('auth.login'))

    return render_template("login.html", form=form)


@auth.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST'and form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user:
            flash ('Username already taken')
            return redirect(url_for('.register'))        
        elif len(username) < 2:
            flash('Username must be greater than 1 character')
            return redirect(url_for('.register'))
        elif len(password) < 2:
            flash('Password should be at least 2 characters')
            return redirect(url_for('.register'))
        else:
            new_user = User(username=username, password=generate_password_hash(
                password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('auth.profile'))
    return render_template("register.html", form=form)
