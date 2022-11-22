"""
User namespace
"""
from src.restx_api import restx_api


event_ns = restx_api.namespace('event', 'Event API')
