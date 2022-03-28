from typing import Dict, Any

from application.dao.directors import DirectorsDAO
from application.services.helpers.schemas.director import DirectorSchema


class DirectorsService:

    def __init__(self, dao: DirectorsDAO, schema: DirectorSchema):
        self.dao = dao
        self.schema = schema

    def get_all(self):
        return self.schema.dump(self.dao.get_all(), many=True)

    def get_one(self, uid: int):
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
