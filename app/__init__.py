from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_rq2 import RQ

rq = RQ()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    rq.init_app(app)
    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes

        db.create_all()  # Create database tables for our data models

        return app
