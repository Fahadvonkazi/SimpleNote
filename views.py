from flask import render_template, request, flash, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from . import db
from .models import Note


views = Blueprint('views', __name__)

@views.route('/notes')
@login_required
def notes():
    return render_template('notes.html', user=current_user)


@views.route('/index')
def index():
    return render_template('index.html', user=current_user)


@views.route('/')
@login_required
def home():
    notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template('notes.html', user=current_user, notes=notes)


@views.route('/add_note', methods=['POST'])
@login_required
def add_note():
    title = request.form.get('title')
    content = request.form.get('content')

    if not title or not content:
        flash('Bitte Titel und Inhalt eingeben!', category='error')
    else:
        new_note = Note(title=title, content=content, author=current_user)
        db.session.add(new_note)
        db.session.commit()
        flash('Notiz erfolgreich hinzugefügt!', category='success')

    return redirect(url_for('views.home'))

@views.route('/edit_note/<int:note_id>', methods=['GET', 'POST'])
@login_required
def edit_note(note_id):
    note = Note.query.get(note_id)

    if request.method == 'POST':
        note.title = request.form.get('title')
        note.content = request.form.get('content')
        db.session.commit()
        flash('Notiz erfolgreich bearbeitet!', category='success')
        return redirect(url_for('views.home'))

    return render_template('edit_note.html', user=current_user, note=note)

@views.route('/delete_note/<int:note_id>')
@login_required
def delete_note(note_id):
    note = Note.query.get(note_id)
    db.session.delete(note)
    db.session.commit()
    flash('Notiz erfolgreich gelöscht!', category='success')
    return redirect(url_for('views.home'))
