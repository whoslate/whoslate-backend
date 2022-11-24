"""
Module for event attendance by event id
"""
from ..restx_namespace import event_ns
from .attend_event import AttendEvent


@event_ns.route('/<int:event_id>/attend')
@event_ns.param('event_id', "Event's ID")
class EventByIdAttendance(
    AttendEvent
):
    """
    This class will inherit other rest controller classes
    """
