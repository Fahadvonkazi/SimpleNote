from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Note

db = SQLAlchemy()

# ... (bisheriger Code bleibt unverändert)

# Füge die unten stehenden Klassen zu deiner db.py hinzu:

# Klasse für Benutzer
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    notes = db.relationship('Note', backref='author', lazy=True)

# Klasse für Notizen
class Note(db.Model):               
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# ... (bisheriger Code bleibt unverändert)

# Hinzufügen der create_all()-Methode für die Initialisierung der Datenbank
with app.app_context():
    db.create_all()
