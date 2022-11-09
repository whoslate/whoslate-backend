"""
User entity
"""
from .database import db


class User(db.Model):
    """
    User table
    """
    user_id = db.Column(
        db.BigInteger,
        db.Sequence('user_id_seq', start=1, increment=1),
        primary_key=True
    )
    phone_number = db.Column(db.String(64), nullable=False)
    phone_country_code = db.Column(db.String(64), nullable=False)
    full_name = db.Column(db.String(64), nullable=False)
    db.UniqueConstraint(phone_number, phone_country_code)

    def __init__(self, phone_number: str, phone_country_code: str):
        self.set_phone_number(phone_country_code=phone_country_code, phone_number=phone_number)

    def set_phone_number(self, phone_country_code: str, phone_number: str):
        """
        Set Phone Number
        :param phone_country_code: such as 1 for US
        :param phone_number: phone number
        :return: void
        """
        self.phone_number = phone_number
        self.phone_country_code = phone_country_code

    def set_full_name(self, full_name: str):
        """
        Set name
        :param full_name: full name
        :return: void
        """
        if len(full_name) > 63:
            raise ValueError('Full name is too long')
        self.full_name = full_name
