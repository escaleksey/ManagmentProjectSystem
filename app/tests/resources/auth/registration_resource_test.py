import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from app.resources.user import UserResource
from app.resources.auth import RegistrationResource
from app.models import User

class TestRegistrationResource(unittest.TestCase):

    @patch("app.resources.registration_resource.User.query")
    @patch("app.resources.registration_resource.requests.post")
    def test_post_user_success(self, mock_post, mock_query):
        mock_query.filter_by.return_value.first.return_value = None
        mock_post.return_value.json.return_value = {"user": {"id": 1, "email": "test@test.com"}}
        mock_post.return_value.status_code = 201

        with patch("app.resources.registration_resource.request.get_json", return_value={
            "email": "test@test.com",
            "password": "password123"
        }):
            resource = RegistrationResource()
            response, status = resource.post()

        self.assertEqual(status, 201)
        self.assertEqual(response, {"user": {"id": 1, "email": "test@test.com"}})

    @patch("app.resources.registration_resource.User.query")
    def test_post_user_already_exists(self, mock_query):
        mock_user = MagicMock()
        mock_query.filter_by.return_value.first.return_value = mock_user

        with patch("app.resources.registration_resource.request.get_json", return_value={
            "email": "test@test.com",
            "password": "password123"
        }):
            resource = RegistrationResource()
            response, status = resource.post()

        self.assertEqual(status, 409)
        self.assertEqual(response, {"message": "User already exists"})
