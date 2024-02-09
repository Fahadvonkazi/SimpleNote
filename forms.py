# Formulare aus Flask-WTF und Validatoren aus WTForms werden importiert
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo

# Formular für die Registrierung
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=7)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), Length(min=7), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

# Formular für die Anmeldung
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')
    
# Formular für Erstellen einer Notiz
class NoteForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(min=5)])
    content = StringField('Content', validators=[InputRequired()])
    submit = SubmitField('Save')

# Formular für das Bearbeiten einer Notiz
class EditNoteForm(FlaskForm):
    id = HiddenField()
    title = StringField('Title', validators=[InputRequired(), Length(min=5)])
    content = StringField('Content', validators=[InputRequired()])
    submit = SubmitField('Update')


'''
### Kommentierter Code für die Weiterentwicklung im nächsten Sprint: Grundidee (noch nicht funktionsfähig) ###

from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField
from wtforms.validators import InputRequired

class NoteForm(FlaskForm):
    placeholder1 = TextAreaField('Placeholder 1', validators=[InputRequired()])
    placeholder2 = TextAreaField('Placeholder 2', validators=[InputRequired()])
    placeholder3 = TextAreaField('Placeholder 3', validators=[InputRequired()])
    placeholder4 = TextAreaField('Placeholder 4', validators=[InputRequired()])
    placeholder5 = TextAreaField('Placeholder 5', validators=[InputRequired()])
    submit = SubmitField('Save')
    '''




