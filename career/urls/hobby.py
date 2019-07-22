from controller.hobby.handlers import (HobbyCreateHandler,
                                       HobbyListHandler)


urls = [
    (r'/hobby/create', HobbyCreateHandler),
    (r'/hobby/list', HobbyListHandler),
]
