from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('theboard')
app.config.from_pyfile('settings.py')

db = SQLAlchemy(app)
