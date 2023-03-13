""" App to work with items depends on its brand"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from app.views import views
