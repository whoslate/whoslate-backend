"""
Module for sign in
"""
from flask_jwt_extended import create_access_token
from flask_restx import Resource
from twilio.base.exceptions import TwilioRestException

from .restx_namespace import user_ns
from .restx_sign_in_response_model import sign_in_response
from ..model import User
from ..utils import verification_check


signin_parser = user_ns.parser()
signin_parser.add_argument('country_code', type=int, required=True)
signin_parser.add_argument('phone_number', type=int, required=True)
signin_parser.add_argument('verification_code', type=int, required=True)


@user_ns.route('/signin')
class Signin(Resource):
    """
    Controller for sign up
    """

    @user_ns.expect(signin_parser)
    @user_ns.marshal_with(sign_in_response)
    def post(self):
        """
        Get phone number, verification code, and full name, then return status and access token
        """
        args = signin_parser.parse_args(strict=True)
        country_code = str(args['country_code'])
        phone_number = str(args['phone_number'])
        code = str(args['verification_code'])
        try:
            verification_result = verification_check(
                phone_country_code=country_code,
                phone_number=phone_number,
                code=code
            )
            if verification_result == 'pending':
                return {
                    'status': 'pending',
                    'msg': 'Your verification code is wrong',
                    'access_token': ''
                }
        except TwilioRestException as err:
            return {
                       'status': 'error',
                       'msg': err.msg,
                       'access_token': ''
                   }, 400
        try:
            user = User.get_user_by_phone(country_code, phone_number)
            if not user:
                user = User.new_user(
                    phone_country_code=country_code,
                    phone_number=phone_number
                )
        except ValueError as err:
            return {
                'status': 'error',
                'msg': err.args[0],
                'access_token': ''
            }, 400

        access_token = create_access_token(identity=user.user_id)
        return {
            'status': 'success',
            'msg': 'Welcome',
            'access_token': access_token
        }, 200
