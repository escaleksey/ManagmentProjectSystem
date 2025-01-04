from flask import Flask, make_response, jsonify
from .routes import user_routes, auth_routes
from .extentions import db, migrate
from .models import User
import os


def create_app():


    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return "KK"
    # Initialize extensions
    #db.init_app(app)
    #migrate.init_app(app, db)

    @app.route('/users', methods=['GET'])
    def get_users():
        try:
            users = User.query.all()
            return make_response(jsonify({"users": [user.json() for user in users]}), 200)

        except Exception as e:
            return make_response(jsonify({"message": str(e)}), 500)

    # Register blueprints
    #app.register_blueprint(user_routes)
    #app.register_blueprint(auth_routes)

    return app