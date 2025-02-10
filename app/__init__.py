import os

from flask import Flask, session
from flask_restful import Api

import logging
from config import init_redis
from .extentions import db, migrate, server_session
from .models import User
from .routes import auth_bp, auth_routes, user_bp, user_routes


def create_app():

    app = Flask(__name__)
    app.config.from_object(os.environ["APP_SETTINGS"])
    app.logger.setLevel(logging.DEBUG)
    db.init_app(app)
    migrate.init_app(app, db)
    init_redis(app)
    server_session.init_app(app)
    api = Api(app)

    @app.route("/")
    def index():
        try:
            return "KK"
        except Exception as e:
            return f"{str(e)}"

    @app.route('/clear_session')
    def clear_session():
        session.clear()
        return "Session cleared", 200


    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/user")
    # Register blueprints
    # app.register_blueprint(user_routes)
    # app.register_blueprint(auth_routes)

    return app
