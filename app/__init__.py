from flask import Flask
#from .routes import user_routes, auth_routes
from extentions import db, migrate
import os


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    migrate.init_app(app, db)
    # Initialize extensions
    #db.init_app(app)
    #migrate.init_app(app, db)

    # Register blueprints
    #app.register_blueprint(user_routes)
    #app.register_blueprint(auth_routes)

    return app