"""
Model the response for sign up
"""

from flask_restx import fields
from .sign_up import api_response
from .restx_namespace import user_ns

sign_up_response = user_ns.inherit('SignUpResponse', api_response, {
    'access_token': fields.String(description='User access token')
})
