from flask import request
from flask_restful import Resource
from werkzeug.routing import ValidationError
from os import environ

from app import Project
from app.models import Task

ERR_MSG_TASK_NAME = "Task already created"
ERR_MSG_ACCESS = "Access denied"
TITLE = "title"
DESCRIPTION = "description"
PROJECT = "project_id"
ROLE = "role_id"
MESSAGE = "message"
VALID_API_KEYS = environ.get("VALID_API_KEYS").split(",")


class TaskResource(Resource):
    def get(self,project_id, _id):
        try:
            task: Task = Task.query.filter_by(id=_id).first()
            if task:
                return task.to_dict(), 200
            return {MESSAGE: []}, 404
        except Exception as e:
            return {MESSAGE: str(e)}, 404

    def put(self, project_id, _id):
        task = Task.query.filter_by(id=_id).first()
        if task:
            data = request.get_json()
            self._validate_task(data[TITLE], data[PROJECT])
            task.title = data.get(TITLE)
            task.description = data.get(DESCRIPTION)
            task.project_id = data.get(PROJECT)
            task.role = data.get(ROLE)



    def delete(self, _id):
        task: Task = Task.query.filter_by(id=_id).first()
        if not task:
            return {MESSAGE: []}, 404
        try:
            task.delete()
            return task.to_dict(), 201
        except Exception as e:
            return {MESSAGE: str(e)}, 500

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
    def _validate_task(title:str, project_id:int):
        tasks = Task.query.where(Task.title == title and Task.project_id == project_id).first()
        if tasks:
            raise ValidationError(ERR_MSG_TASK_NAME)
