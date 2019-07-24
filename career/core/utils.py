import json
import hashlib
from json.decoder import JSONDecodeError


class Validator:
    """请求参数校验
    """

    def __init__(self, args, params=None):
        self.args = args
        self.params = params
        self.value_msg = list()
        self.type_msg = list()
        self.err_msg = ""

    def parse_args(self):
        try:
            self.params = json.loads(self.args)
            return True
        except (TypeError, JSONDecodeError):
            return False

    def arg_check(self,
                   arg_key,
                   arg_type,
                   default=None,
                   nullable=True):
        """请求参数校验
        """
        arg_val = self.params.get(arg_key)

        if not arg_val and default:
            arg_val = default

        # NOTE 参数非空校验
        if not nullable and not arg_val:
            if default:
                arg_val = default
            else:
                self.value_msg.append(arg_key)
                return None

        # NOTE 参数类型校验
        if arg_val and type(arg_val) != arg_type:
            try:
                arg_val = arg_type(arg_val)
            except (ValueError, TypeError):
                self.type_msg.append(arg_key)
                if arg_val:
                    return arg_val
                return None
        return arg_val

    def is_arg_valid(self):
        if self.value_msg:
            value_err = "参数{}为空"
            self.err_msg = value_err.format(",".join(self.value_msg))

        if self.type_msg:
            type_err = "参数{}类型错误"
            self.err_msg = type_err.format(",".join(self.type_msg))

        if self.err_msg:
            return False, self.err_msg
        return True, None


class Encryption:
    """加密
    """

    @staticmethod
    def encrypt(data):
        """加密
        """
        if data:
            obj = hashlib.sha256()
            obj.update(bytes(data, encoding="utf-8"))
            value = obj.hexdigest()
            return value

    @staticmethod
    def decrypt(data):
        """解密
        """
        pass
