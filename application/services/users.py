from typing import Dict, Any

from application.dao.users import UsersDAO
from application.services.helpers.get_hash import get_hash
from application.services.helpers.schemas.user import UserSchema


class UsersService:

    def __init__(self, dao: UsersDAO, schema: UserSchema):
        self.dao = dao
        self.schema = schema

    def get_all(self):
        """Сериализуем всех юзеров"""
        return self.schema.dump(self.dao.get_all(), many=True)

    def get_one(self, uid: int):
        """Сериализуем 1 юзера"""
        return self.schema.dump(self.dao.get_one(uid))

    def update(self, uid: int, data: Dict[str, Any]):
        """Загружаем полученные данные, сериализуем их"""
        return self.schema.dump(self.dao.update(uid, self.schema.load(data)))

    def create(self, data: Dict[str, Any]):
        """Загружаем новые данные, хэшируем пароль, создаем запись, сериализуем ее"""
        hash_password = get_hash(data.get('password'))
        data['password'] = hash_password
        if data.get('role') != 'admin':
            data['role'] = 'user'
        return self.schema.dump(self.dao.create(self.schema.load(data)))

    def delete(self, uid: int):
        """Удаляем запись"""
        return self.dao.delete(uid)


