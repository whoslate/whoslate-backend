"""
Module for attending event
"""
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx import Resource
from src.event_controller.restx_namespace import event_ns
from src.restx_models.api_response import api_response
from src.model.event import Event
from src.model.user import User
from src.model.attendance import Attendance

attend_event_parser = event_ns.parser()
attend_event_parser.add_argument('key_for_attendee', type=str, required=True)


class AttendEvent(Resource):
    """
    Attend event by event id and key
    """

    @event_ns.doc(security='apikey')
    @event_ns.expect(attend_event_parser)
    @event_ns.response(403, 'User not found', api_response)
    @event_ns.response(404, 'Event not found', api_response)
    @event_ns.response(406, 'Key error', api_response)
    @event_ns.response(200, 'Success', api_response)
    @jwt_required()
    def post(self, event_id: int):
        """
        Attend event
        """

        user = User.get_user_by_id(get_jwt_identity())
        if not user:
            return {
                'status': 'error',
                'msg': "I can't find you"
            }, 403
        event = Event.get_event_by_id(event_id)
        if not event:
            return {
               'status': 'error',
               'msg': 'event not found'
           }, 404
        args = attend_event_parser.parse_args(strict=True)

        if event.key_for_attendee != args['key_for_attendee']:
            return {
                'status': 'error',
                'msg': 'key incorrect'
            }, 406

        Attendance.new_attendance(event.event_id, user.user_id)

        return {
            'status': 'success',
            'msg': 'Attended'
        }, 200
