"""
Model the response for sign up
"""

from flask_restx import fields
from src.user_controller.restx_namespace import user_ns
from src.restx_models.api_response import api_response

sign_in_response = user_ns.inherit('SignInResponse', api_response, {
    'access_token': fields.String(description='User access token')
})
