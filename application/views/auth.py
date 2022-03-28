from flask import request
from flask_restx import Resource, Namespace

from application.container import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthsView(Resource):

    def post(self):
        req_json = request.json

        username = req_json.get("username", None)
        password = req_json.get("password", None)
        tokens = auth_service.create_tokens(username=username, password=password)

        return tokens, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token")
        tokens = auth_service.refresh_tokens(refresh_token)

        return tokens, 201
