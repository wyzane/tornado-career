import json
from config.db import engine_db_career
from sqlalchemy.orm import scoped_session, sessionmaker


class ResponseMixin:

    status = {
        "00000": "成功",
        "00001": "参数格式错误",
        "00002": "请求参数错误",
        "00003": "对象不存在",
        "00004": "对象已存在",
        "00005": ""
    }

    def __init__(self, code="00000", msg="成功"):
        self._code = code
        self._msg = msg

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value
        print("self _code:", self._code)

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def json_response(self, data=None):
        resp = {
            "code": self._code,
            "msg": self._msg,
            "data": data
        }
        return resp

