"""
Phone number verification power by Twilio
"""
import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
verify_sid = os.environ['TWILIO_VERIFY_SID']


client = Client(account_sid, auth_token)


def create_verification(phone_country_code: str, phone_number: str):
    """
    Send verification code to phone number
    :param phone_country_code:
    :param phone_number:
    :return: void
    """
    client.verify \
        .v2 \
        .services(verify_sid) \
        .verifications \
        .create(to=f'+{phone_country_code}{phone_number}', channel='sms')


def verification_check(phone_country_code: str, phone_number: str, code: str) -> str:
    """
    Check the verification.
    :param phone_country_code:
    :param phone_number:
    :param code:
    :return:
    'pending' if code is wrong
    'approved' if code is correct
    """
    verification = client.verify \
        .v2 \
        .services(verify_sid) \
        .verification_checks \
        .create(to=f'+{phone_country_code}{phone_number}', code=code)
    return verification.status
