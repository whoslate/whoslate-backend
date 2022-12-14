"""
Module for create a new event
"""
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource

from src.model.user import User
from src.model.event import Event

from src.event_controller.restx_namespace import event_ns
from src.restx_models.api_response import api_response
from src.restx_models.event import event_private_restx_model

new_event_parser = event_ns.parser()
new_event_parser.add_argument('event_name', type=str, required=True)


class NewEvent(Resource):
    """
    Controller for creating new event
    """

    @event_ns.doc(security='apikey')
    @event_ns.expect(new_event_parser)
    @event_ns.response(code=200, model=event_private_restx_model, description='Success')
    @event_ns.response(code=400, model=api_response, description='Error')
    @jwt_required()
    def post(self):
        """
        Create new event
        """
        args = new_event_parser.parse_args(strict=True)
        event_name = args['event_name']
        user = User.get_user_by_id(get_jwt_identity())
        if not user:
            return {
                'status': 'error',
                'msg': 'You disappeared'
            }, 400
        try:
            event = Event.new_event(event_name, user.user_id)
        except ValueError as err:
            return {
                'status': 'error',
                'msg': err.args[0]
            }, 400

        return {
            'event_id': event.event_id,
            'event_name': event.event_name,
            'organizer_user_id': event.organizer_user_id,
            'event_desc': event.event_desc,
            'start_time': event.start_time.isoformat(),
            'key_for_attendee': event.key_for_attendee,
        }
