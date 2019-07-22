from core.utils import Validator
from models.hobby import model
from config.base import PAGE, PAGE_SIZE

from ..common import CommonHandler


DISPLAY_FIELDS = ["id", "desc", "modified",
                  "created", "operator"]


class HobbyCreateHandler(CommonHandler):

    def post(self):
        """创建兴趣
        """
        params = self.request.body
        validator = Validator(args=params)

        # NOTE 解析参数
        if not validator.parse_args():
            self.code = "00001"
            self.msg = "参数格式错误"
            self.json_response()
            self.finish()

        desc = validator.arg_check(
            arg_key="desc",
            arg_type=str,
            nullable=False)
        operator = validator.arg_check(
            arg_key="operator",
            arg_type=str)

        is_arg_valid, err_msg = validator.is_arg_valid()
        if is_arg_valid:
            params = {
                "desc": desc,
                "operator": operator
            }

            tb_career_hobby = model("career_hobby")
            obj = self.db_career.execute(tb_career_hobby
                                         .__table__.insert(),
                                         params)
            self.db_career.commit()
            if obj.is_insert:
                self.json_response()
            else:
                self.code = "00005"
                self.json_response()
        self.code = "00001"
        self.msg = err_msg
        self.json_response()


class HobbyListHandler(CommonHandler):

    def post(self):
        """兴趣列表
        """
        params = self.request.body
        validator = Validator(args=params)

        # NOTE 解析参数
        if not validator.parse_args():
            self.code = "00001"
            self.msg = "参数格式错误"
            self.json_response()
            self.finish()

        hobby_id = validator.arg_check(
            arg_key="hobbyId",
            arg_type=int)
        desc = validator.arg_check(
            arg_key="desc",
            arg_type=str)
        page = validator.arg_check(
            arg_key="page",
            arg_type=int,
            default=PAGE)
        page_size = validator.arg_check(
            arg_key="pageSize",
            arg_type=int,
            default=PAGE_SIZE)

        is_arg_valid, err_msg = validator.is_arg_valid()

        if is_arg_valid:
            tb_career_hobby = model("career_hobby")
            query_obj = self.db_career.query(tb_career_hobby)
            query_con = None

            if hobby_id and desc:
                query_con = {
                    "id": hobby_id,
                    "desc": desc
                }
            elif hobby_id and not desc:
                query_con = {
                    "id": hobby_id
                }
            elif desc and not hobby_id:
                query_con = {
                    "desc": desc
                }

            hobby_objs = self.db_query(query_obj,
                                       query_con,
                                       page,
                                       page_size)

            # FIXME 这种实现方式待优化
            hobby_list = list()
            for hobby in hobby_objs:
                tmp = dict()
                tmp["id"] = hobby.id
                tmp["desc"] = hobby.desc.strip()
                tmp["created"] = str(hobby.created)
                tmp["modified"] = str(hobby.modified)
                tmp["operator"] = hobby.operator.strip()
                hobby_list.append(tmp)
            self.json_response(hobby_list)
        self.code = "00001"
        self.msg = err_msg
        self.json_response()


class HobbyUpdateHandler(CommonHandler):
    """更新兴趣
    """

    def post(self):
        params = self.request.body
        validator = Validator(args=params)

        # NOTE 解析参数
        if not validator.parse_args():
            self.code = "00001"
            self.msg = "参数格式错误"
            self.json_response()
            self.finish()

        hobby_id = validator.arg_check(
            arg_key="hobbyId",
            arg_type=int,
            nullable=False)
        desc = validator.arg_check(
            arg_key="desc",
            arg_type=str)

        is_arg_valid, err_msg = validator.is_arg_valid()
        if is_arg_valid:
            tb_career_hobby = model("career_hobby")
            query_obj = self.db_career.query(tb_career_hobby)
            query_con = {
                "id": hobby_id
            }
            hobby_objs = self.db_query(query_obj,
                                       query_con)

            if hobby_objs:
                # FIXME 待优化
                for hobby in hobby_objs:
                    hobby.desc = desc
                self.db_career.commit()
            self.json_response()
        self.code = "00001"
        self.msg = err_msg
        self.json_response()
