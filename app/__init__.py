""" App to work with items depends on its brand"""

from flask import Flask
from flask_migrate import Migrate
from .config import Config
import sqlalchemy as db


app = Flask(__name__)
app.config.from_object(Config)


# engine = db.create_engine('mysql+pymysql://root:19865421@localhost/items_storage', echo=True)
# connection = engine.connect()
# metadata = db.MetaData()

# migrate = Migrate(app, db)

from app.views import views
