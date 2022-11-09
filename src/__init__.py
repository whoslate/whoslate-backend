"""
Root blueprint
"""
from flask import Blueprint
from .user_blueprint import user_blueprint

root_blueprint: Blueprint = Blueprint('root', __name__)
root_blueprint.register_blueprint(user_blueprint, url_prefix='/user')
