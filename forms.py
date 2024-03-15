from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField
from wtforms.validators import DataRequired, Email, Length

class AddPersonForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone #', validators=[DataRequired(), Length(min=10, max=15)])
    usernames = StringField('Usernames')
    emails = FieldList(StringField('Email'), min_entries=1, validators=[Email()])
    passwords = FieldList(StringField('Password'), min_entries=1, validators=[Length(min=6)])
    birthdays = StringField('Birthday')
    city = StringField('City')
    submit = SubmitField('Add Person')
