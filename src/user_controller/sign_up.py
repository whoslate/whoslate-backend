"""
Module for sign up
"""
from flask_restx import Resource
from src.restx_model import api_response
from .restx_namespace import user_ns


@user_ns.route('/signup/phone_verify')
class PhoneVerifySignUp(Resource):
    """
    Verify user phone number
    """

    @user_ns.marshal_with(api_response)
    def post(self):
        """
        Post method
        :return:
        """
        return {
            'status': 'hi',
            'msg': '123'
        }
