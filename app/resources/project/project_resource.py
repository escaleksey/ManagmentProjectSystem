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


class ProjectResource(Resource):
    def get(self, _id):
        try:
            project = Project.query.filter_by(id=_id).first()
            if project:
                return project.to_dict(), 200
            return {MESSAGE: []}, 404
        except Exception as e:
            return {MESSAGE: str(e)}, 404

    def post(self):
        api_key = request.headers.get("X-API-KEY")

        try:
            self._validate_api_key(api_key)
            user_id = int(session.get('user_id'))
            self._validate_user(user_id)
            data = request.get_json()

            project_name = data['title']
            theme = data['theme']

            self._validate_project_name(project_name, user_id)
            project = Project(title=project_name, theme=theme, creating_date=datetime.now())
            project.save()
            project_member = ProjectMemberRole(user_id=user_id, project_id=project.id, role_id=OWNER_ID)
            project_member.save()


        except Exception as e:
            return {MESSAGE: str(e), "data": request.remote_addr}, 409

    @staticmethod
    def _validate_api_key(api_key: str):
        if api_key not in VALID_API_KEYS:
            raise ValidationError(ERR_MSG_ACCESS)

    @staticmethod
    def _validate_project_name(project_name: str, user_id: int):
        project_exists = db.session.query(Project).join(ProjectMemberRole).filter(
            Project.title == project_name,
            ProjectMemberRole.user_id == user_id
        ).first()

        if project_exists:
            raise ValidationError(ERR_MSG_PROJECT_NAME)

    @staticmethod
    def _validate_user(user_id: int):
        user_exists = User.query.filter(User.id == user_id).first()
        if not user_exists:
            raise ValidationError(ERR_MSG_ACCESS)

