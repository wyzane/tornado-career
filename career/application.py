from tornado import web

from config.base import settings
from config.db import db_career
from urls.routers import routers


"""
路由配置
"""


class Application(web.Application):

    def __init__(self):
        urls = routers
        super(Application, self).__init__(urls, **settings)

        self.db_career = db_career
