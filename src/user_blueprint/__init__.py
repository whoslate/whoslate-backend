"""
Blueprint for user
"""
from flask import Blueprint

user_blueprint: Blueprint = Blueprint('user', __name__)

@user_blueprint.route('/')
def index():
    return 'Hi'
