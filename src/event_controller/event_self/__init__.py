"""
Module for
"""
from src.event_controller.event_self.new_event import NewEvent
from src.event_controller.event_self.get_events import GetEvents
from ..restx_namespace import event_ns


@event_ns.route('/')
class Event(NewEvent, GetEvents):
    """
    This class would inherit others.
    """
