from tornado import ioloop, httpserver

from application import Application
from config import base


if __name__ == '__main__':
    port = base.options.get("port")
    print("server port:", port)

    app = Application()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(port)

    ioloop.IOLoop.current().start()
