# Benötigte Funktionen und Klassen werden aus Flask importiert
from flask import render_template, request, flash, redirect, url_for, Blueprint

# Decorator und aktueller Benutzer werden importiert 
from flask_login import login_required, current_user

# DB wird aus dem Projektordner importiert
from . import db

# Note-Modell wird importiert
from .models import Note

# Blueprint für Ansichten werden erstellt
views = Blueprint('views', __name__)

# Hier sind die Routen zu den verschiedenen Seiten und Aktionen

# Route zur notes.html
@views.route('/notes')
@login_required
def notes():
    return render_template('notes.html', user=current_user)

# Route zur index.html
@views.route('/index')
def index():
    return render_template('index.html', user=current_user)

@views.route('/')
@login_required
def home():
    # Hier werden die Notizen des aktuellen Benutzers aus der DB abgerufen
    notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template('notes.html', user=current_user, notes=notes)


@views.route('/add_note', methods=['POST'])
@login_required
def add_note():
    # Titel- und Inhalt soll aus dem Form extrahiert werden
    title = request.form.get('title')
    content = request.form.get('content')

    # Es wird geprüft, ob Titel und Inhalt vorhanden sind 
    if not title or not content:
        flash('Please enter title and content!', category='error')
    # Notiz wird erstellt und zur DB hinzugefügt
    else:
        new_note = Note(title=title, content=content, author=current_user)
        db.session.add(new_note)
        db.session.commit()
        flash('Note successfully added!', category='success')

    return redirect(url_for('views.home'))

@views.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    # Notiz wird aus DB abgerufen 
    note = Note.query.get(note_id)

    # Titel und Inhalt werden aktualisiert und in der DB gespeichert
    if request.method == 'POST':
        note.title = request.form.get('title')
        note.content = request.form.get('content')
        db.session.commit()
        flash('Note successfully edited!', category='success')
        return redirect(url_for('views.home'))

    return render_template('edit_note.html', user=current_user, note=note)

@views.route('/delete_note/<int:note_id>')
@login_required
def delete_note(note_id):
    # Ausgewählte Notiz soll aus DB gelöscht werden
    note = Note.query.get(note_id)
    db.session.delete(note)
    db.session.commit()
    flash('Note successfully deleted!', category='success')
    return redirect(url_for('views.home'))
