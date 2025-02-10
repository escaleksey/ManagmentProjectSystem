from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session


db = SQLAlchemy()
migrate = Migrate()
server_session = Session()
