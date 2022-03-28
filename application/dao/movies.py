from typing import Dict, Any

from application.dao.models.movie import Movie


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        """Получаем все фильмы (несериализованные)"""
        return self.session.query(Movie).all()

    def get_one(self, uid: int):
        """Получаем 1 фильм (несериализованный)"""
        return self.session.query(Movie).get(uid)

    def update(self, uid: int, data: Dict[str, Any]):
        """Изменяем данные 1 фильма, возвращаем измененный фильм"""
        self.session.query(Movie).filter(Movie.id == uid).update(data)
        self.session.commit()
        return self.get_one(uid)

    def create(self, data: Dict[str, Any]):
        """Добавляем новый фильм, получаем его же"""
        new_movie = Movie(**data)
        self.session.add(new_movie)
        self.session.commit()

        return new_movie

    def delete(self, uid: int):
        delete_movie = self.get_one(uid)
        self.session.delete(delete_movie)
        self.session.commit()
        return ''

    def get_by_director_id(self, director_id: int):
        return self.session.query(Movie).filter(Movie.director_id == director_id)

    def get_by_genre_id(self, genre_id: int):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id)

    def get_by_year(self, year: int):
        return self.session.query(Movie).filter(Movie.year == year)
