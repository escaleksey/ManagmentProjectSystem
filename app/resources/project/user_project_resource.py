from flask import request, session
from flask_restful import Resource
from datetime import datetime
from app.models import Project, User, ProjectMemberRole
from app.extentions import db
from werkzeug.routing import ValidationError
from os import environ


ERR_MSG_PROJECT_NAME = "Project already exists"
ERR_MSG_ACCESS = "Access denied"
OWNER_ID = 1

MESSAGE = "message"
VALID_API_KEYS = environ.get("VALID_API_KEYS").split(",")


class UserProjectResource(Resource):
    def get(self, user_id):
        try:

            if not user_id:
                return {MESSAGE: "Unauthorized"}, 401

            # Получаем все project_id, где пользователь участвует
            project_ids = db.session.query(ProjectMemberRole.project_id).filter_by(user_id=user_id).subquery()

            # Получаем проекты
            projects = Project.query.filter(Project.id.in_(project_ids)).all()

            return {"projects": [p.to_dict() for p in projects]}, 200

        except Exception as e:
            return {MESSAGE: str(e)}, 500




    @staticmethod
    def _validate_user(user_id: int):
        user_exists = User.query.filter(User.id == user_id).first()
        if not user_exists:
            raise ValidationError(ERR_MSG_ACCESS)

