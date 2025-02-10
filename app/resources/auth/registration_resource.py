import requests
from flask import request
from flask_restful import Resource
from os import environ
from app.models import User
from app.routes import USER_URL
VALID_API_KEYS = environ.get("VALID_API_KEYS").split(",")

class RegistrationResource(Resource):
    def post(self):
        data = request.get_json()

        email = data["email"]
        password = data["password"]

        user = User.query.filter_by(email=email).first()

        if user:
            return {"message": "User already exists"}, 409

        headers = {
            'X-API-KEY': VALID_API_KEYS[0],
            "Content-Type": "application/json"}
        response = requests.post(USER_URL, json=data, headers=headers)

        return response.json(), response.status_code
