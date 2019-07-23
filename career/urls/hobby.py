from controller.hobby.handlers import (HobbyCreateHandler,
                                       HobbyListHandler,
                                       HobbyUpdateHandler,
                                       HobbyDeleteHandler)


urls = [
    (r'/api/v1/hobby/create', HobbyCreateHandler),
    (r'/api/v1/hobby/list', HobbyListHandler),
    (r'/api/v1/hobby/update', HobbyUpdateHandler),
    (r'/api/v1/hobby/delete', HobbyDeleteHandler),
]
