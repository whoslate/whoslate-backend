"""
Module for event by id
"""
from ..restx_namespace import event_ns
from .get_event import GetEvent
from .set_event import SetEvent

@event_ns.route('/<int:event_id>')
@event_ns.param('event_id', "Event's ID")
class EventById(
    GetEvent,
    SetEvent
):
    """
    This class will inherit other rest controller classes
    """
