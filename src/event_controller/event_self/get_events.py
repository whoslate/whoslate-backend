"""
Module for get events that hosted by myself
"""
from typing import List

from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource, fields
from src.event_controller.restx_namespace import event_ns
from src.model import Event
from src.model.user import User
from src.restx_models.api_response import api_response
from src.restx_models.event import event_private_restx_model


class GetEvents(Resource):
    """
    Controller for get all events
    """

    @event_ns.doc(security='apikey')
    @event_ns.response(code=400, model=api_response, description='Error')
    @event_ns.response(
        code=200,
        model=fields.List(fields.Nested(event_private_restx_model)),
        description='Success'
    )
    @jwt_required()
    def get(self):
        """
        Get all events hosted by myself
        """
        user = User.get_user_by_id(get_jwt_identity())
        if not user:
            return {
                'status': 'error',
                'msg': 'You disappeared'
            }, 400

        events = get_events_by_user(user)
        return events


def get_events_by_user(user: User):
    """
    Get list of event by user object
    :param user: user
    :return: list of event
    """
    raw_events: List[Event] = user.events
    events = []
    for raw_event in raw_events:
        event = {
            'event_id': raw_event.event_id,
            'event_name': raw_event.event_name,
            'organizer_user_id': raw_event.organizer_user_id,
            'event_desc': raw_event.event_desc,
            'start_time': raw_event.start_time.isoformat(),
            'key_for_attendee': raw_event.key_for_attendee
        }
        events.append(event)
    return events
