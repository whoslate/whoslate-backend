"""
Test for User model
"""
from src.model.user import User
TEST_PHONE_NUMBER = '987654321'
TEST_COUNTRY_CODE = '1'
ALTER_PHONE_NUMBER = '12345454'
ALTER_COUNTRY_CODE = '2'
TEST_FULL_NAME = 'Linbin Pang'


def test_init(app):
    """
    Remove previous testing data
    :param app:
    :return:
    """
    with app.app_context():
        User.delete_user_by_phone(TEST_COUNTRY_CODE, TEST_PHONE_NUMBER)
        User.delete_user_by_phone(ALTER_COUNTRY_CODE, ALTER_PHONE_NUMBER)


def test_new_user(app):
    """
    Create User Test
    :param app:
    :return:
    """
    with app.app_context():
        test_user = User.new_user(TEST_COUNTRY_CODE, TEST_PHONE_NUMBER)
        assert isinstance(test_user, User)


def test_query_and_update(app):
    """
    User Query Test
    User update full name, phone number, password Test
    :param app:
    :return:
    """
    with app.app_context():
        test_user = User.get_user_by_phone(TEST_COUNTRY_CODE, TEST_PHONE_NUMBER)
        assert isinstance(test_user, User)
        test_user.set_phone_number(ALTER_COUNTRY_CODE, ALTER_PHONE_NUMBER)
        test_user.set_full_name('John Doe')
        test_user.set_password('123456')
        test_user.save()
        test_user.set_phone_number(TEST_COUNTRY_CODE, TEST_PHONE_NUMBER)
        test_user.save()


def test_delete_user(app):
    """
    User Delete Test
    :param app:
    :return:
    """
    with app.app_context():
        test_user = User.get_user_by_phone(TEST_COUNTRY_CODE, TEST_PHONE_NUMBER)
        test_user.delete()
