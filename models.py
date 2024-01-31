from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy() 

class User(db.Model, UserMixin):    #Erstellen des Datenbankmodells für Benutzer
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.string(100), nullable=False)
    notes = db.relationship('Note', backref='author', lazy=True)

class Note(db.Model):               #Erstellen des Datenbankmodells für Notizen
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), Nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
