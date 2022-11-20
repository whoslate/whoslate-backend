"""
Module for sign up
"""
from flask_restx import Resource
from twilio.base.exceptions import TwilioRestException

from src.restx_api_response_model import api_response
from .restx_namespace import user_ns
from ..model import User
from ..utils import create_verification, verification_check

phone_number_parser = user_ns.parser()
phone_number_parser.add_argument('country_code', type=int, required=True)
phone_number_parser.add_argument('phone_number', type=int, required=True)


@user_ns.route('/signup/get_verification_code')
class GetPhoneVerificationCodeForSignUp(Resource):
    """
    Get verification code for sign up
    """

    @user_ns.expect(phone_number_parser)
    @user_ns.marshal_with(api_response)
    def post(self):
        """
        Get phone number and return status
        :return:
        """
        args = phone_number_parser.parse_args(strict=True)
        country_code = str(args['country_code'])
        phone_number = str(args['phone_number'])
        is_existed = True
        try:
            user = User.get_user_by_phone(
                phone_country_code=country_code,
                phone_number=phone_number
            )
            if not user:
                is_existed = False
        except Exception: # pylint: disable=broad-except
            return {
                'status': 'error',
                'msg': 'Internal Error'
            }, 500

        if is_existed:
            return {
                'status': 'error',
                'msg': 'Phone number existed'
            }, 400

        try:
            create_verification(
                phone_country_code=country_code,
                phone_number=phone_number
            )
        except TwilioRestException as err:
            return {
                'status': 'error',
                'msg': err.msg
            }, 400

        return {
            'status': 'success',
            'msg': 'Message has been sent'
        }, 200


phone_number_verify_parser = user_ns.parser()
phone_number_verify_parser.add_argument('country_code', type=int, required=True)
phone_number_verify_parser.add_argument('phone_number', type=int, required=True)
phone_number_verify_parser.add_argument('verification_code', type=int, required=True)
phone_number_verify_parser.add_argument('full_name', type=str, required=True)

@user_ns.route('/signup/check_verification_code')
class CheckPhoneVerificationCodeForSignUp(Resource):
    """
    After get the verification code, check if verification code is valid
    """

    @user_ns.expect(phone_number_verify_parser)
    @user_ns.marshal_with(api_response)
    def post(self):
        """
        Get phone number, verification code, and full name, then return status
        :return:
        """
        args = phone_number_verify_parser.parse_args(strict=True)
        country_code = str(args['country_code'])
        phone_number = str(args['phone_number'])
        code = str(args['verification_code'])
        full_name = str(args['full_name'])
        try:
            verification_result = verification_check(
                phone_country_code=country_code,
                phone_number=phone_number,
                code=code
            )
            if verification_result == 'pending':
                return {
                    'status': 'pending',
                    'msg': 'Your verification code is wrong'
                }
        except TwilioRestException as err:
            return {
                'status': 'error',
                'msg': err.msg
            }, 400

        try:
            User.new_user(
                phone_country_code=country_code,
                phone_number=phone_number,
                full_name=full_name
            )
        except ValueError as err:
            return {
                'status': 'error',
                'msg': err.args[0]
            }, 400
        return {
            'status': 'success',
            'msg': 'Account has been created'
        }, 200
