from flask import jsonify, make_response, request
from flask_restful import Resource
from werkzeug.routing import ValidationError

from app.models import User

ERR_MSG_EMAIL = "Email already registered"
USERNAME = "username"
ABOUT = "about"
EMAIL = "email"
PASSWORD = "password"
MESSAGE = "message"

class UserResource(Resource):
    def get(self, _id):
        user = User.query.filter_by(id=id).first()
        if user:
            return user.to_dict(), 200
        return {MESSAGE: []}, 404

    def put(self, _id):
        user = User.query.filter_by(id=_id).first()
        if not user:
            return {MESSAGE: []}, 404
        try:
            data = request.get_json()
            user.username = data[USERNAME]
            user.about = data[ABOUT]
            user.email = data[EMAIL]
            user.password = data[PASSWORD]
            user.save()
            return user.to_dict(), 201
        except Exception as e:
            return {MESSAGE: str(e)}, 500

    def post(self):
        data = request.get_json()
        try:
            self._validate_email(data[EMAIL])
            new_user = User(
                username=data[USERNAME],
                about=data[ABOUT],
                email=data[EMAIL], password=data[PASSWORD])
            new_user.save()
            return new_user.to_dict(), 201
        except Exception as e:
            return {MESSAGE: str(e)}, 400

    def delete(self, _id):
        user = User.query.filter_by(id=_id).first()
        if not user:
            return {MESSAGE: []}, 404
        try:
            user.delete()
            return user.to_dict(), 201
        except Exception as e:
            return {MESSAGE: str(e)}, 500

    def _validate_email(self, email):
        email = User.query.filter_by(email=email).all()
        if email:
            raise ValidationError(ERR_MSG_EMAIL)
