"""
Module for get other_user profile
"""
from flask_jwt_extended import jwt_required
from flask_restx import Resource

from src.user_controller.restx_user_info_model import user_public_info_model
from ..restx_namespace import user_ns
from ...restx_api_response_model import api_response
from ...model import User


class GetUserProfile(Resource):
    """
    Get other_user profile
    """

    @user_ns.doc(security='apikey')
    @jwt_required()
    @user_ns.response(200, model=user_public_info_model, description='Success')
    @user_ns.response(404, model=api_response, description='User not found')
    def get(self, user_id: int):
        user = User.get_user_by_id(user_id)
        if not user:
            return {
                'status': 'error',
                'msg': 'other_user not found'
            }, 404
        return {
                'user_id': user.user_id,
                'full_name': user.full_name
            }, 200
