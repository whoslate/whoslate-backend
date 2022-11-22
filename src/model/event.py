"""
Model for event
"""
from datetime import datetime
from uuid import uuid4
from .database import db
# pylint: disable=no-member


class Event(db.Model):
    """
    Event table
    """
    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_name = db.Column(db.String(128), nullable=False)
    organizer_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    event_desc = db.Column(db.Text, nullable=True)
    start_time = db.Column(db.DateTime)
    key_for_attendee = db.Column(db.String(64), nullable=False)
    attendances = db.relationship('Attendance', backref='event', lazy=True)

    def __init__(self, event_name: str, organizer_user_id: int):
        self.set_event_name(event_name)
        self.key_for_attendee = str(uuid4())
        self.organizer_user_id = organizer_user_id
        self.start_time = datetime.utcnow()

    def set_event_name(self, event_name: str):
        """
        Set event name
        :param event_name:
        :return:
        """
        if len(event_name) > 127:
            raise ValueError('Event name is too long')
        self.event_name = event_name

    def set_event_desc(self, event_desc: str):
        """
        Set event description
        :param event_desc:
        :return:
        """
        self.event_desc = event_desc

    def delete(self):
        """
        Delete event
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
    def get_event_by_id(cls, event_id: int):
        """
        Get event by ID
        :param event_id:
        :return:
        """
        event: cls = cls.query.filter_by(
            event_id=event_id
        ).first()
        return event

    @classmethod
    def delete_event_by_event_name(cls, event_name: str):
        """
        Delete event by event name
        :param event_name:
        :return:
        """
        event = cls.query.filter_by(event_name=event_name).first()
        if event:
            db.session.delete(event)
            cls.save()


    @classmethod
    def new_event(cls, event_name: str, organizer_user_id: int):
        """
        Create a new event
        :param event_name:
        :param organizer_user_id:
        :return:
        """
        event = cls(event_name, organizer_user_id)
        db.session.add(event)
        cls.save()
        return event
