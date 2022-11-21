"""
Module for accessing other user
"""
from .get_user_profile import GetUserProfile
from .update_user_profile import UpdateUserProfile
from ..restx_namespace import user_ns


@user_ns.route('/<int:user_id>')
@user_ns.param('user_id', "User's ID")
class OtherUser(
    GetUserProfile
):
    """
    This class will inherit other rest controller classes
    """
