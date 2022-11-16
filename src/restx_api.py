"""
Module for storing restx api and namespace
"""
from flask_restx import Api
from .blueprint import api_blueprint


restx_api = Api(api_blueprint,
                version='0.1',
                title='API',
                description='API for every thing'
                )
