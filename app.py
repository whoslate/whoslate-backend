"""
Flask entry
"""
import os
from flask import Flask
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

from src.model import db, migrate
from src import api_blueprint

load_dotenv()


def create_app() -> Flask:
    """
    App factory
    :return: app
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
    db.init_app(app)
    migrate.init_app(app, db)
    JWTManager(app)
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
