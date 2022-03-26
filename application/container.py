from application.dao.directors import DirectorsDAO
from application.dao.genres import GenresDAO
from application.dao.movies import MoviesDAO
from application.database import db
from application.services.directors import DirectorsService
from application.services.genres import GenresService
from application.services.movies import MoviesService
from application.services.schemas.director import DirectorSchema
from application.services.schemas.genre import GenreSchema
from application.services.schemas.movie import MovieSchema

movies_schema = MovieSchema()
movies_dao = MoviesDAO(db.session)
movies_service = MoviesService(movies_dao, movies_schema)

genres_schema = GenreSchema()
genres_dao = GenresDAO(db.session)
genres_service = GenresService(genres_dao, genres_schema)

directors_schema = DirectorSchema()
directors_dao = DirectorsDAO(db.session)
directors_service = DirectorsService(directors_dao, directors_schema)
