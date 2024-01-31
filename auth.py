from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .import db 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash('Erfolgreich eingeloggt!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        else:
            flash('Falsche E-Mail oder Passwort! Versuchen Sie es erneut!', category='error')

    return render_template('login.html', user=current_user)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('E-Mail existiert bereits!', category='error')
        elif len(email) < 4:
            flash('E-Mail muss länger als drei Zeichen sein!', category='error')
        elif len(username) < 2:
            flash('Benutzername muss länger als ein Zeichen sein!', category='error')
        elif password1 != password2:
            flash('Passwörter stimmen nicht überein!', category='error')
        elif len(password1) < 7:
            flash('Passwort muss mindestens sieben Zeichen lang sein!', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Registrierung erfolgreich!', category='success')
            return redirect(url_for('views.home'))

    return render_template('register.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Erfolgreich ausgeloggt!', category='success')
    return redirect(url_for('auth.login'))