"""
Module for restx
"""
from flask_restx import fields

from src import restx_api

user_public_info_model = restx_api.model('UserPublicInfo', {
    'user_id': fields.Integer(description='User ID'),
    'full_name': fields.String(description='User full name')
}, description='Response from getting a other_user information')

user_private_info_model = restx_api.inherit('UserPrivateInfo', user_public_info_model, {
    'phone_number': fields.String(description='User phone number'),
    'phone_country_code': fields.String(description='User phone country code')
})
