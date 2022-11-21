"""
Model the response for sign up
"""

from flask_restx import fields
from .restx_namespace import user_ns
from ..restx_api_response_model import api_response

sign_in_response = user_ns.inherit('SignInResponse', api_response, {
    'access_token': fields.String(description='User access token')
})
