import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
from tornado.options import options,define
import os

define('port',default=8088,type=int,help='please input port')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class hello_module(tornado.web.UIModule):
    def render(self):
        return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[
        (r'/',IndexHandler)
    ],
    template_path=os.path.join(os.path.dirname(__file__),'templates'),
    ui_modules={'hello':hello_module}
    )
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
