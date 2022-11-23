"""
Module for change the configuration of event
"""
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource
from ..restx_namespace import event_ns
from ...model.event import Event
from ...restx_models.api_response import api_response

update_event_parser = event_ns.parser()
update_event_parser.add_argument('event_name', type=str, required=False)
update_event_parser.add_argument('event_desc', type=str, required=False)


class SetEvent(Resource):
    """
    Controller for configurate an event
    """

    @event_ns.doc(security='apikey')
    @jwt_required()
    @event_ns.expect(update_event_parser)
    @event_ns.response(200, 'Success', api_response)
    @event_ns.response(404, 'Event not found', api_response)
    @event_ns.response(401, 'Unauthorized', api_response)
    @event_ns.response(400, 'Error', api_response)
    def put(self, event_id: int):
        """
        Edit the event
        """
        event = Event.get_event_by_id(event_id)
        if not event:
            return {
                'status': 'error',
                'msg': 'event not found'
            }, 404
        if event.organizer_user_id != get_jwt_identity():
            return {
                'status': 'error',
                'msg': 'Unauthorized'
            }, 401

        event_info = update_event_parser.parse_args(strict=True)
        try:
            if event_info['event_name']:
                event.set_event_name(event_info['event_name'])
            if event_info['event_desc']:
                event.set_event_desc(event_info['event_desc'])
        except ValueError as err:
            return {
               'status': 'error',
               'msg': err.args[0]
            }, 400

        event.save()
        return {
            'status': 'success',
            'msg': 'Event updated'
        }
