"""
Controller for get verification code
"""
from flask_restx import Resource
from twilio.base.exceptions import TwilioRestException
from .restx_namespace import user_ns
from ..utils import create_verification
from ..restx_models.api_response import api_response

phone_number_parser = user_ns.parser()
phone_number_parser.add_argument('country_code', type=int, required=True)
phone_number_parser.add_argument('phone_number', type=int, required=True)


@user_ns.route('/get_verification_code')
class GetVerificationCode(Resource):
    """
    Controller for get verification code
    """

    @user_ns.expect(phone_number_parser)
    @user_ns.marshal_with(api_response)
    def post(self):
        """
        Input phone number, then you will receive verification code
        """
        args = phone_number_parser.parse_args(strict=True)
        country_code = str(args['country_code'])
        phone_number = str(args['phone_number'])
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
