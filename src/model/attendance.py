"""
Model for Attendance, connecting user and event entities
"""
from datetime import datetime
from .database import db
# pylint: disable=no-member


class Attendance(db.Model):
    """
    Attendance module
    """
    attendance_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime)
    event_id = db.Column(db.Integer, db.ForeignKey('event.event_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def __init__(self, event_id: int, user_id: int):
        self.event_id = event_id
        self.user_id = user_id
        self.time = datetime.utcnow()

    def delete(self):
        """
        Delete attendance
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
    def new_attendance(cls, event_id: int, user_id: int):
        """
        Creat a new attendance
        :param event_id:
        :param user_id:
        :return:
        """
        attend: cls = cls(event_id, user_id)
        db.session.add(attend)
        cls.save()
        return attend
