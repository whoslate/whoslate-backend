"""
Module for get my profile
"""
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource

from src.user_controller.restx_user_info_model import user_private_info_model
from ..restx_namespace import user_ns
from ...restx_api_response_model import api_response
from ...model import User


class GetMyProfile(Resource):
    """
    Get my profile
    """

    @user_ns.doc(security='apikey')
    @jwt_required()
    @user_ns.response(200, model=user_private_info_model, description='Success')
    @user_ns.response(404, model=api_response, description='User not found')
    def get(self):
        """
        Get my profile
        """
        user = User.get_user_by_id(get_jwt_identity())
        if not user:
            return {
                'status': 'error',
                'msg': 'My profile is missing'
            }, 404
        return {
                'user_id': user.user_id,
                'full_name': user.full_name,
                'phone_number': user.phone_number,
                'phone_country_code': user.phone_country_code
            }, 200
