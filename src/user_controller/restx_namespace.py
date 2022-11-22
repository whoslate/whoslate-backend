"""
User namespace
"""
from src.restx_api import restx_api


user_ns = restx_api.namespace('user', 'User API')
