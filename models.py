# UserMixin-Klasse und DB werden importiert
from flask_login import UserMixin
from . import db

#Erstellen des Datenbankmodells für Benutzer
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    notes = db.relationship('Note', backref='author', lazy=True)

#Erstellen des Datenbankmodells für Notizen
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#Erstellen des Datenbankmodells für Pages
class Pages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    notes_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)