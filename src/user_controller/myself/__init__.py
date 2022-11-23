"""
Module for accessing myself
"""
from ..restx_namespace import user_ns
from .get_my_profile import GetMyProfile
from .sign_in import Signin


@user_ns.route('/')
class MySelf(GetMyProfile, Signin):
    """
    This class will inherit other rest controller classes
    """
