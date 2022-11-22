"""
Model for event
"""
from flask_restx import fields

from .restx_namespace import event_ns

event_restx_model = event_ns.model('Event', {
    'event_id': fields.Integer(description='Event ID'),
    'event_name': fields.String(description='Event Name'),
    'organizer_user_id': fields.String(description="Organizer's user ID"),
    'event_desc': fields.String(description='Event description'),
    'start_time': fields.DateTime(description='Time when event is created'),
    'key_for_attendee': fields.String(description='Key for attendee')
})
