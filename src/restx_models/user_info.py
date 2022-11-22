"""
Module for restx
"""
from flask_restx import fields

from src.user_controller.restx_namespace import user_ns

user_public_info_model = user_ns.model('UserPublicInfo', {
    'user_id': fields.Integer(description='User ID'),
    'full_name': fields.String(description='User full name')
}, description='Response from getting a other_user information')

user_private_info_model = user_ns.inherit('UserPrivateInfo', user_public_info_model, {
    'phone_number': fields.String(description='User phone number'),
    'phone_country_code': fields.String(description='User phone country code')
})
