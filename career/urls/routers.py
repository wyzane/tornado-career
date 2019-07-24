from controller.index import IndexHandler
from .hobby import urls as url_hobby
from .account import urls as url_account


routers = [
    (r'/index', IndexHandler),
]

routers += url_hobby
routers += url_account
