
from flask_restful import Resource

from app.models import Role


class RoleListResource(Resource):
    def get(self):
        users = Role.query.all()
        if users:
            return [user.to_dict() for user in users], 200
        return {"message": []}, 404
