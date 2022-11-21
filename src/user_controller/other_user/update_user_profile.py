from flask_restx import Resource

from ..restx_namespace import user_ns


class UpdateUserProfile(Resource):
    def put(self, user_id: int):
        return f'{user_id}'
