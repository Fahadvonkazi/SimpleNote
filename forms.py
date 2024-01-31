from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length

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
    email = StringField('Email', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=3)])
    email = StringField('Email', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired(), Length(min=7)])
    confirm_password = StringField('Confirm Password', validators=[InputRequired(), Length(min=7)])
    submit = SubmitField('Register')
