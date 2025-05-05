import os

from flask import Flask, session
from flask_restful import Api

import logging
from config import init_redis
from .extentions import db, migrate, server_session
from .models import User, Role, Project, ProjectMemberRole, Stage
from .routes import auth_bp, auth_routes, user_bp, user_routes, project_bp


def seed_roles():
    default_roles = ["Автор", "Менеджер", "Разработчик", "Тестировщик"]

    for title in default_roles:
        existing = Role.query.filter_by(title=title).first()
        if not existing:
            role = Role(title=title)
            role.save()


def seed_stages():
    default_stages = ["Не начато", "В работе", "Тестирование", "Сделано"]

    for title in default_stages:
        existing = Stage.query.filter_by(title=title).first()
        if not existing:
            stage = Stage(title=title)
            stage.save()


def create_app():

    app = Flask(__name__)
    app.config.from_object(os.environ["APP_SETTINGS"])
    app.logger.setLevel(logging.DEBUG)
    db.init_app(app)
    migrate.init_app(app, db)
    init_redis(app)
    server_session.init_app(app)
    api = Api(app)

    with app.app_context():

        seed_roles()
        seed_stages()

    @app.route("/")
    def index():
        try:
            return session.get("user_id")
        except Exception as e:
            return f"{str(e)}"

    @app.route('/clear_session')
    def clear_session():
        session.clear()
        return "Session cleared", 200


    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(project_bp, url_prefix="/project")
    # Register blueprints
    # app.register_blueprint(user_routes)
    # app.register_blueprint(auth_routes)

    return app



