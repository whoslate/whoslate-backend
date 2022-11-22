"""
Test for event model
"""
from datetime import datetime

from src import User
from src.model.event import Event
TEST_PHONE_NUMBER = '987654321'
TEST_COUNTRY_CODE = '1'
TEST_EVENT_NAME = 'Class'
TEST_ORGANIZER_USER_ID = ''
TEST_EVENT_DESC = 'Hello'


def test_init(app):
    """
    Remove previous testing data
    and create testing user
    :param app:
    :return:
    """
    with app.app_context():
        Event.delete_event_by_event_name(TEST_EVENT_NAME)
        test_user = User.get_user_by_phone(TEST_COUNTRY_CODE, TEST_PHONE_NUMBER)
        if not test_user:
            User.new_user(TEST_COUNTRY_CODE, TEST_PHONE_NUMBER)


def test_new_event_and_query(app):
    """
    Create new event
    :param app:
    :return:
    """
    with app.app_context():
        test_user = User.get_user_by_phone(TEST_COUNTRY_CODE, TEST_PHONE_NUMBER)
        test_event = Event.new_event(TEST_EVENT_NAME, test_user.user_id)
        test_event.set_event_desc(TEST_EVENT_DESC)
        assert isinstance(test_event, Event)
        assert isinstance(test_event.start_time, datetime)
        assert isinstance(test_event.key_for_attendee, str)
        assert isinstance(test_event.event_desc, str)
        event = Event.get_event_by_id(test_event.event_id)
        assert isinstance(event, Event)
