from flask import Flask, make_response, jsonify
from flask_restful import Api
from .routes import user_routes, auth_routes
from .extentions import db, migrate
from .models import User
from .resources import UserResource, UserListResource
import os


def create_app():

    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    migrate.init_app(app, db)
    api = Api(app)

    @app.route('/')
    def index():
        return "KK"

    api.add_resource(UserResource, '/user', '/user/<int:_id>')
    api.add_resource(UserListResource, '/users')
    # Register blueprints
    #app.register_blueprint(user_routes)
    #app.register_blueprint(auth_routes)

    return app