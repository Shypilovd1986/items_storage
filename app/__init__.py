""" App to work with items depends on its brand"""

from flask import Flask
from flask_migrate import Migrate
from .config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.views import views
