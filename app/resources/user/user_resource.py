from flask import request
from flask_restful import Resource
from werkzeug.routing import ValidationError
from os import environ
from app.models import User

ERR_MSG_EMAIL = "Email already registered"
ERR_MSG_ACCESS = "Access denied"
USERNAME = "username"
ABOUT = "about"
EMAIL = "email"
PASSWORD = "password"
MESSAGE = "message"
VALID_API_KEYS = environ.get("VALID_API_KEYS").split(",")


class UserResource(Resource):
    def get(self, _id):
        try:
            user = User.query.filter_by(id=_id).first()
            if user:
                return user.to_dict(), 200
            return {MESSAGE: []}, 404
        except Exception as e:
            return {MESSAGE: str(e)}, 404

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
        api_key = request.headers.get("X-API-KEY")

        try:
            self._validate_api_key(api_key)
            self._validate_email(data[EMAIL])
            new_user = User(
                username=data[USERNAME],
                about=data[ABOUT],
                email=data[EMAIL],
                password=data[PASSWORD],
            )
            new_user.save()
            return {"user": new_user.to_dict(), "data": request.remote_addr}, 201
        except Exception as e:
            return {MESSAGE: str(e), "data": request.remote_addr}, 409

    def delete(self, _id):
        user = User.query.filter_by(id=_id).first()
        if not user:
            return {MESSAGE: []}, 404
        try:
            user.delete()
            return user.to_dict(), 201
        except Exception as e:
            return {MESSAGE: str(e)}, 500

    @staticmethod
    def _validate_email(email):
        email = User.query.filter_by(email=email).all()
        if email:
            raise ValidationError(ERR_MSG_EMAIL)

    @staticmethod
    def _validate_api_key(api_key: str):
        if api_key not in VALID_API_KEYS:
            raise ValidationError(ERR_MSG_ACCESS)
