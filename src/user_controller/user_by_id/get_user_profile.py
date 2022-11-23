"""
Module for get user profile by id
"""
from flask_jwt_extended import jwt_required
from flask_restx import Resource

from src.restx_models.user_info import user_public_info_model
from ..restx_namespace import user_ns
from ...restx_models.api_response import api_response
from ...model import User


class GetUserProfile(Resource):
    """
    Get user profile by id
    """

    @user_ns.doc(security='apikey')
    @jwt_required()
    @user_ns.response(200, model=user_public_info_model, description='Success')
    @user_ns.response(404, model=api_response, description='User not found')
    def get(self, user_id: int):
        """
        Get user's profile by user id
        """
        user = User.get_user_by_id(user_id)
        if not user:
            return {
                'status': 'error',
                'msg': 'user not found'
            }, 404
        return {
                'user_id': user.user_id,
                'full_name': user.full_name
            }, 200
