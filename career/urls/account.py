from controller.account.handlers import RegisterHandler, LoginHandler


urls = [
    (r'/api/v1/user/register', RegisterHandler),
    (r'/api/v1/user/login', LoginHandler),
]