import os

class config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///ai.db'
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_TRACK_MODIFICATIONS = True