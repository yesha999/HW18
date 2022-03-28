from flask import request
from flask_restx import Resource, Namespace

from application.container import directors_service
from application.services.helpers.decorators import auth_required, admin_required
from application.services.helpers.schemas import director

directors_ns = Namespace('directors')
director_schema = director.DirectorSchema()
directors_schema = director.DirectorSchema(many=True)


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):

    @auth_required
    def get(self, uid):
        return directors_service.get_one(uid), 200

    @admin_required
    def put(self, uid):
        return directors_service.update(uid, request.json), 200

    @admin_required
    def delete(self, uid):
        return directors_service.delete(uid), 204


@directors_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self):
        return directors_service.get_all()

    @admin_required
    def post(self):
        return directors_service.create(request.json), 201
