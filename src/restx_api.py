"""
Module for storing restx api and namespace
"""
from flask_restx import Api
from .blueprint import api_blueprint


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': 'The format of value should be: "Bearer [access_token]"'
    }
}

restx_api = Api(api_blueprint,
                version='0.1',
                title='API',
                description='API for every thing',
                authorizations=authorizations
                )
