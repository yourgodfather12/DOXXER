from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    usernames = db.Column(db.String(100))
    emails = db.Column(db.String(200))
    passwords = db.Column(db.String(200))
    birthdays = db.Column(db.String(100))
    city = db.Column(db.String(100))

class AddPersonForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone #', validators=[DataRequired()])
    usernames = StringField('Usernames')
    emails = StringField('Emails')
    passwords = StringField('Passwords')
    birthdays = StringField('Birthdays')
    city = StringField('City')
    submit = SubmitField('Add Person')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Validate login credentials
        # Redirect to dashboard if successful
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Register new user
        # Redirect to login page
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    # Access user's dashboard
    # Provide options to add, search, display, export, and import data
    return render_template('dashboard.html')

@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    form = AddPersonForm()
    if form.validate_on_submit():
        new_person = Person(
            name=form.name.data,
            phone=form.phone.data,
            usernames=form.usernames.data,
            emails=form.emails.data,
            passwords=form.passwords.data,
            birthdays=form.birthdays.data,
            city=form.city.data
        )
        db.session.add(new_person)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_person.html', form=form)

@app.route('/search_person', methods=['GET', 'POST'])
def search_person():
    if request.method == 'POST':
        # Search for person in the database
        # Display contact window with person's information
        return render_template('search_person.html')
    return render_template('search_person.html')

@app.route('/display_people')
def display_people():
    # Display all people in the database
    return render_template('display_people.html')

@app.route('/export_data', methods=['POST'])
def export_data():
    # Export database to different formats
    return redirect(url_for('dashboard'))

@app.route('/import_data', methods=['POST'])
def import_data():
    # Import data into the database
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
