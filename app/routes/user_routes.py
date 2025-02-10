from flask import Blueprint, session
from flask_restful import Api
import requests
from app.resources.user import UserListResource, UserResource
from .urls import USER_URL

user_bp = Blueprint("user", __name__, url_prefix="/user")
user_api = Api(user_bp)

user_api.add_resource(UserResource, "", "/<int:_id>")
user_api.add_resource(UserListResource, "/users")

@user_bp.route("/me")
def get_current_user():
    user_id = session.get("user_id")
    if not user_id:
        return {'message': 'User does not exist'}, 401

    user = requests.get(f"{USER_URL}/{user_id}")
    return user.json()

