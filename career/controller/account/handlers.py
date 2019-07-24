from core.utils import Validator, Encryption
from models.account import TB_CAREER_USER

from ..common import CommonHandler


DISPLAY_FIELDS = ["id", "username", "phone", "email",
                  "age", "role", "modified", "created",
                  "operator", "is_deleted"]


class RegisterHandler(CommonHandler):
    """用户注册接口
    """

    def post(self):
        params = self.request.body
        validator = Validator(args=params)

        if not validator.parse_args():
            self.code = "00001"
            self.msg = "参数格式错误"
            self.json_response()

        username = validator.arg_check(
            arg_key="username",
            arg_type=str,
            nullable=False)
        password = validator.arg_check(
            arg_key="password",
            arg_type=str,
            nullable=False)
        phone = validator.arg_check(
            arg_key="phone",
            arg_type=str)
        email = validator.arg_check(
            arg_key="email",
            arg_type=str)
        age = validator.arg_check(
            arg_key="age",
            arg_type=int)
        operator = validator.arg_check(
            arg_key="operator",
            arg_type=str)

        is_arg_valid, err_msg = validator.is_arg_valid()
        if is_arg_valid:
            params = {
                "username": username,
                "password": Encryption.encrypt(password),
                "phone": phone,
                "email": email,
                "age": age,
                "operator": operator
            }

            # 校验用户名是否存在
            query_obj = self.db_career.query(TB_CAREER_USER)
            found = self.db_query(query_obj,
                                  {"username": username})
            if found:
                self.code = "00004"
                self.msg = "用户名已存在"
                self.json_response()

            obj = self.db_career.execute(TB_CAREER_USER.
                                         __table__.insert(),
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


class LoginHandler(CommonHandler):
    """用户登录接口
    """

    def post(self):
        pass