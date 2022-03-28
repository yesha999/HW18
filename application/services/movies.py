from typing import Dict, Any

from application.dao.movies import MoviesDAO
from application.services.helpers.schemas.movie import MovieSchema


class MoviesService:

    def __init__(self, dao: MoviesDAO, schema: MovieSchema):
        self.dao = dao
        self.schema = schema

    def get_all(self):
        """Сериализуем все фильмы"""
        return self.schema.dump(self.dao.get_all(), many=True)

    def get_one(self, uid: int):
        """Сериализуем 1 фильм"""
        return self.schema.dump(self.dao.get_one(uid))

    def update(self, uid: int, data: Dict[str, Any]):
        """Загружаем полученные данные, сериализуем их"""
        return self.schema.dump(self.dao.update(uid, self.schema.load(data)))

    def create(self, data: Dict[str, Any]):
        """Загружаем новые данные, создаем запись, сериализуем ее"""
        return self.schema.dump(self.dao.create(self.schema.load(data)))

    def delete(self, uid: int):
        """Удаляем запись"""
        return self.dao.delete(uid)

    def get_by_director_id(self, director_id: int):
        return self.schema.dump(self.dao.get_by_director_id(director_id), many=True)

    def get_by_genre_id(self, genre_id: int):
        return self.schema.dump(self.dao.get_by_genre_id(genre_id), many=True)

    def get_by_year(self, year: int):
        return self.schema.dump(self.dao.get_by_year(year), many=True)
