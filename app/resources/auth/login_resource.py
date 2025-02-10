from flask import request, session
from flask_restful import Resource

from app.models import User


class LoginResource(Resource):
    def post(self):
        data = request.get_json()

        email = data["email"]
        password = data["password"]

        user = User.query.filter_by(email=email).first()

        if not user:
            return {"message": "User not found", "data": request.remote_addr}, 401

        if not user.check_password(password):
            return {"message": "Wrong password"}, 401

        session["user_id"] = str(user.id).encode('utf-8')
        return {"message": "Login successful"}, 200
