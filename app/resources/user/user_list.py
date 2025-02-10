
from flask_restful import Resource

from app.models import User


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        if users:
            return [user.to_dict() for user in users], 200
        return {"message": []}, 404
