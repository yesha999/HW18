import calendar
import datetime
import hmac

import jwt
from flask_restx import abort

from application.constants import SECRET_HERE
from application.dao.users import UsersDAO
from application.services.helpers.get_hash import get_hash


class AuthService:
    def __init__(self, dao: UsersDAO):
        self.dao = dao

    def create_tokens(self, username, password):

        if None in [username, password]:
            abort(400)

        user = self.dao.get_by_username(username)

        if user is None:
            return {"error": "Неверные учётные данные"}, 401

        password_hash = get_hash(password)

        if hmac.compare_digest(password_hash.encode('utf-8'), user.password.encode('utf-8')) is False:
            return {"error": "Неверные учётные данные"}, 401

        data = {"username": user.username,
                "role": user.role}
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        data["refresh_token"] = False
        access_token = jwt.encode(data, SECRET_HERE, 'HS256')
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        data["refresh_token"] = True
        refresh_token = jwt.encode(data, SECRET_HERE, 'HS256')
        tokens = {"access_token": access_token, "refresh_token": refresh_token}
        return tokens

    def put(self, refresh_token):
        if refresh_token is None:
            abort(400)
        try:
            data = jwt.decode(jwt=refresh_token, key=SECRET_HERE, algorithms=['HS256'])
        except Exception as e:
            abort(400)

        username = data.get("username")

        user = self.dao.get_by_username(username)

        data = {
            "username": user.username,
            "role": user.role
        }
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        data["refresh_token"] = False
        access_token = jwt.encode(data, SECRET_HERE, algorithm=['HS256'])
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        data["refresh_token"] = True
        refresh_token = jwt.encode(data, SECRET_HERE, algorithm=['HS256'])
        tokens = {"access_token": access_token, "refresh_token": refresh_token}

        return tokens, 201
