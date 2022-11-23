"""
Event controller
"""
from .restx_namespace import *
from .new_event import NewEvent
from .get_events import GetEvents
from .restx_namespace import event_ns


@event_ns.route('/')
class Event(NewEvent, GetEvents):
    """
    This class would inherit others.
    """
