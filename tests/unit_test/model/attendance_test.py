"""
Test for Attendance model
"""
from datetime import datetime

from src.model.user import User
from src.model.event import Event
from src.model.attendance import Attendance


TEST_PHONE_NUMBER = '987654321'
TEST_COUNTRY_CODE = '1'
TEST_EVENT_NAME = 'Class'
TEST_ORGANIZER_USER_ID = ''


def test_init(app):
    """
    Remove previous testing data
    Create testing user
    Create testing attendance
    :param app:
    :return:
    """
    with app.app_context():
        Event.delete_event_by_event_name(TEST_EVENT_NAME)
        test_user = User.get_user_by_phone(TEST_COUNTRY_CODE, TEST_PHONE_NUMBER)
        if not test_user:
            User.new_user(TEST_COUNTRY_CODE, TEST_PHONE_NUMBER)


def test_create_attendance(app):
    """
    Create user, event, and attendance
    :param app:
    :return:
    """
    with app.app_context():
        test_user = User.get_user_by_phone(TEST_COUNTRY_CODE, TEST_PHONE_NUMBER)
        event = Event.new_event(TEST_EVENT_NAME, test_user.user_id)
        attendance = Attendance.new_attendance(event.event_id, test_user.user_id)
        Attendance.new_attendance(event.event_id, test_user.user_id)
        assert isinstance(attendance.time, datetime)
        test_user.delete()
        event.delete()
        attendance.delete()
