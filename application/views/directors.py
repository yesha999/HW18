from flask import request
from flask_restx import Resource, Namespace

from application.container import directors_service
from application.services.schemas import director

directors_ns = Namespace('directors')
director_schema = director.DirectorSchema()
directors_schema = director.DirectorSchema(many=True)


@directors_ns.route('/<int:uid>')
class DirectorView(Resource):

    def get(self, uid):
        return directors_service.get_one(uid), 200

    def put(self, uid):
        return directors_service.update(uid, request.json), 200

    def delete(self, uid):
        return directors_service.delete(uid), 204


@directors_ns.route('/')
class MoviesView(Resource):

    def get(self):
        return directors_service.get_all()
