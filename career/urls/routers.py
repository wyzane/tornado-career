from controller.index import IndexHandler
from .hobby import urls as url_hobby


routers = [
    (r'/index', IndexHandler),
]

routers += url_hobby
