"""
Model for restx
"""
from flask_restx import fields
from .restx_api import restx_api


api_response = restx_api.model('APIResponse', {
    'status': fields.String(description='Status of the API response'),
    'msg': fields.String(description='Additional message for that response')
}, description='Normal API response')
