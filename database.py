from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    usernames = db.Column(db.String(100))
    emails = db.Column(db.String(200))
    passwords = db.Column(db.String(200))
    birthdays = db.Column(db.String(100))
    city = db.Column(db.String(100))
