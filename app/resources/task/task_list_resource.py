
from flask_restful import Resource
from os import environ
from app.models import Task, Project

from flask import request
from flask_restful import Resource
from werkzeug.routing import ValidationError

ERR_MSG_TASK_NAME = "Task already created"
ERR_MSG_ACCESS = "Access denied"
TITLE = "title"
DESCRIPTION = "description"
PROJECT = "project_id"
ROLE = "role_id"
MESSAGE = "message"
VALID_API_KEYS = environ.get("VALID_API_KEYS").split(",")


class TaskListResource(Resource):
    def get(self, project_id):
        tasks = Task.query.filter_by(project_id=project_id).all()
        return [task.to_dict() for task in tasks], 200

    def post(self, project_id):
        data = request.get_json()
        api_key = request.headers.get("X-API-KEY")

        try:
            self._validate_api_key(api_key)
            self._validate_project(project_id)
            self._validate_task(data[TITLE], project_id)
            new_task = Task(
                title=data[TITLE],
                description=data[DESCRIPTION],
                project_id=project_id
            )
            new_task.save()
            return {"task": new_task.to_dict(), "data": request.remote_addr}, 201
        except Exception as e:
            return {MESSAGE: str(e), "data": request.remote_addr}, 409

    @staticmethod
    def _validate_api_key(api_key: str):
        if api_key not in VALID_API_KEYS:
            raise ValidationError(ERR_MSG_ACCESS)

    @staticmethod
    def _validate_project(project_id: int):
        project = Project.query.filter_by(id=project_id).first()
        if project is None:
            raise ValidationError(ERR_MSG_ACCESS)

    @staticmethod
    def _validate_task(title: str, project_id: int):
        tasks = Task.query.where(Task.title == title and Task.project_id == project_id).first()
        if tasks:
            raise ValidationError(ERR_MSG_TASK_NAME)