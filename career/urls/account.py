from controller.account.handlers import RegisterHandler


urls = [
    (r'/api/v1/user/register', RegisterHandler),
]