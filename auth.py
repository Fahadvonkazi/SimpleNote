from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db, LoginManager
from .forms import RegistrationForm

auth = Blueprint('auth', __name__)

def load_user(user_id):
    return User.query.get(int(user_id))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Der Benutzername ist bereits vergeben. Bitte wählen Sie einen anderen.', 'error')
        else:
            new_user = User(username=form.username.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()

            flash('Erfolgreich registriert! Bitte einloggen.', 'success')
            return redirect(url_for('views.index'))

    return render_template('register.html', form=form, signup_success=False)

# Importe und Konfigurationen ...

@auth.route('/check_database')
def check_database():
    # Alle Benutzer abrufen
    all_users = User.query.all()

    # Ausgabe der Benutzerinformationen
    for user in all_users:
        print(f"ID: {user.id}, Username: {user.username}, Password: {user.password}")

    return "Überprüfung der Datenbank abgeschlossen."

# Weitere Routen und Konfigurationen ...


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if not user:
            flash('Benutzer nicht gefunden. Überprüfen Sie Ihren Benutzernamen.', category='error')
        else:
            print(f"User found in the database: {user.username}")
            print(f"Stored password hash: {user.password}")

            if check_password_hash(user.password, password):
                login_user(user)
                flash('Erfolgreich eingeloggt!', category='success')
                print(session)  # Debug-Ausgabe für die Session
                return redirect(url_for('views.notes'))
            else:
                flash('Falsches Passwort! Versuchen Sie es erneut.', category='error')

    return render_template('index.html', user=current_user)



@auth.route('/logout')
def logout():
    logout_user()
    flash('Erfolgreich ausgeloggt!', category='success')
    return redirect(url_for('auth.login'))
