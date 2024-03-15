from app import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    usernames = db.Column(db.String(100))
    birthdays = db.Column(db.Date)
    city = db.Column(db.String(100))

    emails = db.relationship('Email', backref='person', lazy=True)
    passwords = db.relationship('Password', backref='person', lazy=True)

    def __repr__(self):
        return f"<Person {self.name}>"


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    def __repr__(self):
        return f"<Email {self.email}>"


class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(200), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    def __repr__(self):
        return f"<Password {self.password}>"
