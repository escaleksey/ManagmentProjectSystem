from flask import Blueprint
from flask_restful import Api

from app.resources.auth import LoginResource, RegistrationResource

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")
auth_api = Api(auth_bp)

auth_api.add_resource(LoginResource, "/login")
auth_api.add_resource(RegistrationResource, "/registration")
