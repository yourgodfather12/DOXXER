import os

class Config:
    # Set the secret key for the application
    SECRET_KEY = os.environ.get('aba3f905a679df54cb233a261242c4d39a0199066ada1b5f') or 'supersecretkey'

    # Configure the database URI
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
