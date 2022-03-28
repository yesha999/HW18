from flask import request
from flask_restx import Resource, Namespace

from application.services.helpers.decorators import auth_required, admin_required
from application.services.helpers.schemas import genre
from application.container import genres_service

genres_ns = Namespace('genres')
genre_schema = genre.GenreSchema()
genres_schema = genre.GenreSchema(many=True)


@genres_ns.route('/<int:uid>')
class GenreView(Resource):

    @auth_required
    def get(self, uid):
        return genres_service.get_one(uid), 200

    @admin_required
    def put(self, uid):
        return genres_service.update(uid, request.json), 200

    @admin_required
    def delete(self, uid):
        return genres_service.delete(uid), 204



@genres_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self):

        return genres_service.get_all()