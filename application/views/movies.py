from flask import request
from flask_restx import Resource, Namespace

from application.services.helpers.schemas import movie
from application.container import movies_service
from application.services.helpers.decorators import auth_required, admin_required

movies_ns = Namespace('movies')
movie_schema = movie.MovieSchema()
movies_schema = movie.MovieSchema(many=True)


@movies_ns.route('/<int:uid>')
class MovieView(Resource):

    @auth_required
    def get(self, uid):
        return movies_service.get_one(uid), 200

    @admin_required
    def put(self, uid):
        return movies_service.update(uid, request.json), 200

    @admin_required
    def delete(self, uid):
        return movies_service.delete(uid), 204


@movies_ns.route('/')
class MoviesView(Resource):

    @auth_required
    def get(self):
        args = request.args
        if 'director_id' in args:
            return movies_service.get_by_director_id(args['director_id']), 200

        if 'genre_id' in args:
            return movies_service.get_by_genre_id(args['genre_id']), 200

        if 'year' in args:
            return movies_service.get_by_year(args['year']), 200

        return movies_service.get_all(), 200

    @admin_required
    def post(self):

        return movies_service.create(request.json), 201
