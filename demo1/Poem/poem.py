import tornado.ioloop
import tornado.httpserver
import tornado.web
import tornado.options
from tornado.options import options,define
import os
define('port',default=8088,type=int,help='please input port')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class PoemHandler(tornado.web.RequestHandler):
    def post(self):
        num1=self.get_argument('num1')
        num2=self.get_argument('num2')
        self.render('poem.html',one=num1,two=num2)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app=tornado.web.Application(
        handlers=[
        (r'/',IndexHandler),
        (r'/poem',PoemHandler)
        ],
        template_path=os.path.join(os.path.dirname(__file__),'templates')
    )
    http=tornado.httpserver.HTTPServer(app)
    http.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
