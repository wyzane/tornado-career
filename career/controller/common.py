from tornado.web import RequestHandler, Finish
from sqlalchemy.ext.serializer import loads, dumps


class CommonHandler(RequestHandler):

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
    }

    def initialize(self):
        self._code = "00000"
        self._msg = "成功"

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

    def json_response(self, data=None):
        """返回response

        Args:
             data: 返回前端的数据

        Returns:

        """
        resp = {
            "code": self.code,
            "msg": self.msg,
            "data": data
        }
        # self.set_header("Content-Type", "application/json; charset=UTF-8")
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
        :param obj:
        :param con:
        :return:
        """
        if con:
            found = obj.filter_by(**con).exists()
        else:
            found = obj.exists()
        return True if found else False
