from tornado.web import RequestHandler, Finish
from pycket.session import SessionMixin

from config.base import NONE_TOKEN_URLS
from core.utils import TokenUtils


class CommonHandler(RequestHandler, SessionMixin):

    status = {
        "00000": "成功",
        "00001": "参数格式错误",
        "00002": "请求参数错误",
        "00003": "对象不存在",
        "00004": "对象已存在",
        "00005": "创建失败",
        "00006": "获取数据失败",
        "00007": "删除失败",
        "00008": "更新失败",
        "00009": "登录失败",
        "00010": "注册失败",
        "00011": "用户未登录"
    }

    def initialize(self):
        self._code = "00000"
        self._msg = "成功"

    def prepare(self):
        """登录校验
        """
        req_url = self.request.uri
        req_auth = (self.request.headers
                    .get("Authentication"))

        if req_url not in NONE_TOKEN_URLS:
            if not req_auth:
                self.code = "00011"
                self.msg = "用户未登录"
                self.json_response()
            else:
                status, msg = (TokenUtils
                               .verify_token(req_auth))
                if not status:
                    self.code = "00011"
                    self.msg = msg
                    self.json_response()
                else:
                    self.auth = msg

    @property
    def db_career(self):
        return self.application.db_career

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def json_response(self, data=None, others=None):
        """返回response

        Args:
             data: 返给前端的数据

        Returns:

        """
        resp = {
            "code": self.code,
            "msg": self.msg,
            "data": data
        }
        if others and type(others) == dict:
            resp = {**resp, **others}
        self.write(resp)
        # self.finish()
        raise Finish()

    def format_data(self, objs, fields=[]):
        """model对象序列化

        Args:
            objs: 待序列化对象
            fields: 显示的字段

        Returns:

        """
        pass

    def db_query(self, obj, con, page=None, page_size=None):
        """查询model对象列表

        Args:
            obj: query对象
            con: 查询条件
            page: 第几页
            page_size: 每页数据条数

        Returns:

        """
        if page and page_size:
            if con:
                found = (obj.filter_by(**con)
                         .limit(page_size)
                         .offset((page - 1) * page_size).all())
            else:
                found = (obj.limit(page_size)
                         .offset((page - 1) * page_size).all())
        else:
            if con:
                found = obj.filter_by(**con).all()
            else:
                found = obj.all()
        return found

    def db_query_first(self, obj, con):
        """查询一个model对象

        Args:
            obj: query对象
            con: 查询条件

        Returns:

        """
        if con:
            found = obj.filter_by(**con).first()
        else:
            found = obj.first()
        return found

    def db_existed(self, obj, con):
        """判断model对象是否存在
        """
        if con:
            found = obj.filter_by(**con).exists()
        else:
            found = obj.exists()
        return True if found else False

    def get_current_user(self):
        # user = self.get_secure_cookie("user")
        user = self.session.get("user")
        if user:
            return user
        return None
