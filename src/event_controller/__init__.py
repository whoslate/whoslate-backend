"""
Event controller
"""
from .restx_namespace import *
from .new_event import NewEvent
from .restx_namespace import event_ns


@event_ns.route('/')
class Event(NewEvent):
    """
    This class would inherit others.
    """
