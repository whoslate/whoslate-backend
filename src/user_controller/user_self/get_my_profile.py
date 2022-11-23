"""
Module for get my profile
"""
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource

from src.restx_models.user_info import user_private_info_model
from ..restx_namespace import user_ns
from ...restx_models.api_response import api_response
from ...model import User


update_profile_parser = user_ns.parser()
update_profile_parser.add_argument('fullname', type=str, required=False)

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

    @user_ns.doc(security='apikey')
    @jwt_required()
    @user_ns.expect(update_profile_parser)
    @user_ns.response(404, model=api_response, description='User not found')
    @user_ns.response(400, model=api_response, description='Data Error')
    @user_ns.response(200, model=api_response, description='Success')
    def put(self):
        """
        Update my profile
        """
        user = User.get_user_by_id(get_jwt_identity())
        if not user:
            return {
                'status': 'error',
                'msg': 'My profile is missing'
            }, 404
        user_info = update_profile_parser.parse_args(strict=True)
        if user_info['fullname']:
            try:
                user.set_full_name(user_info['fullname'])
            except ValueError as err:
                return {
                    'status': 'error',
                    'msg': err.args[0]
                }, 400

        user.save()
        return {
            'status': 'success',
            'msg': 'Your profile has been saved'
        }
