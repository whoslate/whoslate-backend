"""
Flask entry
"""
import os
from flask import Flask
from dotenv import load_dotenv
from src.model import db, migrate
from src import root_blueprint

load_dotenv()


def create_app() -> Flask:
    """
    App factory
    :return: app
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(root_blueprint, url_prefix='/api')

    return app
