from flask import Blueprint, session
from flask_restful import Api
import requests
from app.resources.task import TaskResource
from .urls import USER_URL

task = Blueprint("task", __name__, url_prefix="/task")
task_api = Api(task)


task_api.add_resource(TaskResource, "/")