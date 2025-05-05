from flask import Blueprint, session
from flask_restful import Api
import requests
from app.resources.project import RoleListResource, ProjectResource, UserProjectResource
from app.resources.task import TaskResource, TaskListResource
from .urls import USER_URL

project_bp = Blueprint("project", __name__, url_prefix="/project")
project_api = Api(project_bp)


project_api.add_resource(RoleListResource, "/roles")
project_api.add_resource(ProjectResource, "/")


project_api.add_resource(TaskListResource, "/<int:project_id>/tasks")
project_api.add_resource(TaskResource, "/<int:project_id>/tasks/<int:_id>")

project_api.add_resource(UserProjectResource, "/<int:user_id>/projects")
