from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import app, db, LoginManager
from .forms import RegistrationForm

auth = Blueprint('auth', __name__)

def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()

        flash('Successful signed up! Please Log In!', 'success')

        return redirect(url_for('index'))
    return render_template('register.html', form=form, signup_success=False)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print(f"Attempted login with username: {username} and password: {password}")

        user = User.query.filter_by(username=username).first()

        if user:
            print(f"User found in the database: {user.username}")
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Erfolgreich eingeloggt!', category='success')
                return redirect(url_for('views.notes'))
            else:
                flash('Falsches Passwort! Versuchen Sie es erneut.', category='error')
        else:
            flash('Benutzer nicht gefunden. Überprüfen Sie Ihren Benutzernamen.', category='error')

    return render_template('index.html', user=current_user)

@auth.route('/logout')
def logout():
    logout_user()
    flash('Erfolgreich ausgeloggt!', category='success')
    return redirect(url_for('auth.login'))
