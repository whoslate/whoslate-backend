"""
Module for get event details by id
"""
from flask_jwt_extended import jwt_required
from flask_restx import Resource
from ..restx_namespace import event_ns
from ...restx_models.api_response import api_response
from ...model.event import Event
from ...restx_models.event import event_public_restx_model


class GetEvent(Resource):
    """
    Get event details by event id (public event only)
    """

    @event_ns.doc(security='apikey')
    @jwt_required()
    @event_ns.response(200, model=event_public_restx_model, description='Success')
    @event_ns.response(404, model=api_response, description='Event not found')
    def get(self, event_id: int):
        """
        Get event profile by event id
        """
        event = Event.get_event_by_id(event_id)
        if not event:
            return {
                'status': 'error',
                'msg': 'event not found'
            }, 404

        return {
            'event_id': event.event_id,
            'event_name': event.event_name,
            'organizer_user_id': event.organizer_user_id,
            'event_desc': event.event_desc,
            'start_time': event.start_time.isoformat()
        }
