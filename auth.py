# Module und Klassen aus Flask werden importiert
from flask import Blueprint, render_template, redirect, url_for, flash, request

# Funktionen und Klassen aus Flask-Login und Werkzeug werden importiert
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

# User-Modell, Registrieruns-Forms und DB-Verbindung werden importiert
from .models import User
from . import db, LoginManager
from .forms import RegistrationForm

# Blueprint für Authentifizierurng wird definiert
auth = Blueprint('auth', __name__)

# Funktion zum Laden eines Benutzers anhand seiner ID 
def load_user(user_id):
    return User.query.get(int(user_id))

# Route für die Registrierung von Benutzern
@auth.route('/register', methods=['GET', 'POST'])
def register():
    # RegistrationsForm-Objekt wird erstellt
    form = RegistrationForm()
    # Wenn Formular validiert wurde, indem Post-request mit Daten gesendet wurde, überprüfe, ob ein Benutzer mit dem angegebenen Benutzernamen bereits existiert 
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        # Wenn Benutzer existiert, dann Fehlermeldung ausgeben
        if existing_user:
            flash('The username is already taken. Please choose another one.', 'error')
        else:
            # Passwort wird gehasht mit pbkdf2: sha 256-Methode
            hashed_password = generate_password_hash(form.password.data, method='pbkdf2:sha256')
            # Neuen Benutzer erstellen und zur Datenbank hinzufügen
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            #Ausgabe einer Erfolgsmeldung und Weiterleitung zur Login-Page zum direkten Einloggen nach erfolgreichem Registrieren
            flash('Successfully registered! Please log in.', 'success')
            return redirect(url_for('views.index'))
    # Registerformular wird gerendert
    return render_template('register.html', form=form, signup_success=False)

# Route für die Überprüfung der Benutzer in der Datenbank zum Debuggen 
@auth.route('/check_database')
def check_database():
    # Alle Benutzer werden abgerufen
    all_users = User.query.all()

    # Ausgabe der Benutzerinformationen
    for user in all_users:
        print(f"ID: {user.id}, Username: {user.username}, Password: {user.password}")
    # Ausgabe einer Bestätigung
    return "Überprüfung der Datenbank abgeschlossen."

# Route zum Einloggen von Benutzern
@auth.route('/login', methods=['GET', 'POST'])
def login():
    #Wenn request empfangen wird und Formular gesendet wurde, nehme Benutzernamen und Passwort aus dem Formular
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Aussgabe der Anmeldeinformationen zum Debuggen 
        print(f"Received login request for username: {username}, password: {password}")
        
        #Abgleich des eingebenen Benutzernamens mit den Nutzern in der Datenbank
        user = User.query.filter_by(username=username).first()

        #Wenn Benutzer in DB nicht gefunden wurde, wird Fehlermeldung ausgegeben. Wenn doch, gib Benutzer und Passworthash aus (wieder zum Debuggen)
        if not user:
            flash('User not found. Please check your username.', category='error')
        else:
            print(f"User found in the database: {user.username}")
            print(f"Stored password hash: {user.password}")
        #PW wird mit gespeichertem PW-hash verglichen. Wenn PW korrekt, dann wird der Benutzer eingeloggt, direkt zur notes.html weitergeleitet und Erfolgsmeldung ausgegeben.
            if check_password_hash(user.password, password):
                login_user(user)
                flash('Successfully logged in!', category='success')
                return redirect(url_for('views.notes'))
            # Wenn PW inkorrekt eingegeben, dann wird eine Fehlermeldung ausgegeben.
            else:
                flash('Wrong password. Please try again', category='error')
    # Das Login-Formular wird gerendert
    return render_template('index.html', user=current_user)

# Route für das Ausloggen von Benutzern
@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    # Logge den aktuellen Benutzer aus
    logout_user()

    # Gib eine Erfolgsmeldung aus und leite Benutzer zur Login Seite weiter.
    flash('Successfully logged out!', category='success')
    return redirect(url_for('auth.login'))

'''
### Kommentierter Code für die Weiterentwicklung im nächsten Sprint: Grundidee (noch nicht funktionsfähig) ###

from flask import render_template, redirect, url_for
from . import db, auth  # Replace 'your_flask_app' with the actual name of your Flask application
from .models import Note
from .forms import NoteForm

@auth.route('/create_note', methods=['GET', 'POST'])
@login_required  # Assuming you want to require login to create a note
def create_note():
    form = NoteForm()

    if form.validate_on_submit():
        # Create a new Note instance and save it to the database
        new_note = Note(
            placeholder1=form.placeholder1.data,
            placeholder2=form.placeholder2.data,
            placeholder3=form.placeholder3.data,
            placeholder4=form.placeholder4.data,
            placeholder5=form.placeholder5.data,
            user_id=current_user.id  # Assuming you have a user ID, replace it with the actual user ID
        )

        db.session.add(new_note)
        db.session.commit()

        return redirect(url_for('views.index'))  # Redirect to the index page or wherever you want to go after saving the note

    return render_template('create_note.html', form=form)
    '''
