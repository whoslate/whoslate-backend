"""
Model for event
"""
from flask_restx import fields

from src.restx_api import restx_api

event_public_restx_model = restx_api.model('EventPublic', {
    'event_id': fields.Integer(description='Event ID'),
    'event_name': fields.String(description='Event Name'),
    'organizer_user_id': fields.String(description="Organizer's user ID"),
    'event_desc': fields.String(description='Event description'),
    'start_time': fields.DateTime(description='Time when event is created')
})

event_private_restx_model = restx_api.inherit('EventPrivate', event_public_restx_model, {
    'key_for_attendee': fields.String(description='Key for attendee')
})
