from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db, LoginManager
from .forms import RegistrationForm
from flask import request

auth = Blueprint('auth', __name__)

def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        username = form.username.data
        password1 = form.password.data
        password2 = form.confirm_password.data

        if len(username) < 2:
            flash('Benutzername muss länger als ein Zeichen sein!', category='error')
        elif password1 != password2:
            flash('Passwörter stimmen nicht überein!', category='error')
        elif len(password1) < 7:
            flash('Passwort muss mindestens sieben Zeichen lang sein!', category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Registrierung erfolgreich! Bitte logge dich ein.', category='success')
            return redirect(url_for('auth.login'))

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
