from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo

class NoteForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(), Length(min=5)])
    content = StringField('Content', validators=[InputRequired()])
    submit = SubmitField('Save')

class EditNoteForm(FlaskForm):
    id = HiddenField()
    title = StringField('Title', validators=[InputRequired(), Length(min=5)])
    content = StringField('Content', validators=[InputRequired()])
    submit = SubmitField('Update')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=7)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), Length(min=7), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')
