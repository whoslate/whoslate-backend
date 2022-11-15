"""
Fixtures
"""
import pytest
from flask import Flask
from app import create_app


@pytest.fixture()
def app():
    """
    Get the app
    :return: Flask app
    """
    new_app: Flask = create_app()
    new_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    new_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = None
    return new_app


@pytest.fixture()
def runner(app):
    """
    Run the flask app for testing
    :return:
    """
    app.test_cli_runner()
