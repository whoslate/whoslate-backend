"""
User entity
"""
import hashlib
from .database import db


class User(db.Model):
    """
    User table
    """
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.String(64), nullable=False)
    phone_country_code = db.Column(db.String(64), nullable=False)
    full_name = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
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
        if len(phone_number) > 63:
            raise ValueError('Your phone number is too long')
        if len(phone_country_code) > 63:
            raise ValueError('Your phone number country code is too long')
        if not phone_number.isnumeric():
            raise ValueError('Your phone number should be number')
        if not phone_country_code.isnumeric():
            raise ValueError('Your country code should be number')
        user: User = User.query.filter_by(
            phone_number=phone_number,
            phone_country_code=phone_country_code
        ).first()
        if user is not None:
            raise ValueError('Your phone number has already been used')
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

    def set_password(self, password: str):
        """
        Setting up the password
        :param password: password
        :return: void
        """
        if len(password) < 6:
            raise ValueError('Password is too short')
        if len(password) > 63:
            raise ValueError('Password is too long')
        self.password = hashlib.md5(password.encode()).hexdigest()

    def delete(self):
        """
        Delete user
        :return: void
        """
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        """
        Method for commit the data change to database
        :return:
        """
        db.session.commit()

    @classmethod
    def get_user_by_phone(cls, phone_country_code: str, phone_number: str):
        """
        Query user by phone
        :param phone_country_code:
        :param phone_number:
        :return: user object or None
        """
        user: cls = cls.query.filter_by(
            phone_number=phone_number,
            phone_country_code=phone_country_code
        ).first()
        return user

    @classmethod
    def delete_user_by_phone(cls, phone_country_code: str, phone_number: str):
        """
        Delete user by phone number
        :param phone_country_code: such as '1'
        :param phone_number: such as '9877632'
        :return: void
        """
        user = cls.get_user_by_phone(
            phone_number=phone_number,
            phone_country_code=phone_country_code
        )
        if user is not None:
            db.session.delete(user)
            cls.save()

    @classmethod
    def new_user(cls, phone_country_code: str, phone_number: str):
        """
        Create new user
        :param full_name:
        :param phone_country_code:
        :param phone_number:
        :return: new user
        """
        new_user: cls = cls(phone_number, phone_country_code)
        db.session.add(new_user)
        cls.save()
        return new_user
