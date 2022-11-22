"""
Module for accessing myself
"""
from ..restx_namespace import user_ns
from .get_my_profile import GetMyProfile


@user_ns.route('/')
class Me(GetMyProfile):
    """
    This class will inherit other rest controller classes
    """
