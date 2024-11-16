from flask import Flask
from flask_migrate import Migrate
from flaskbackendmultipledb.config import MultidbConfig
from flaskbackendmultipledb.database import db


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "My_Secret_Key"
    )
    app.config.from_object(MultidbConfig)
    db.init_app(app)
    migrate = Migrate(app, db)
    return app