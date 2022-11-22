"""
Model the response for sign up
"""

from flask_restx import fields

from src import restx_api
from src.restx_models.api_response import api_response

sign_in_response = restx_api.inherit('SignInResponse', api_response, {
    'access_token': fields.String(description='User access token')
})
