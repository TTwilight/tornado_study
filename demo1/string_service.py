from tornado import httpserver,ioloop,web
import tornado.options
from tornado.options import define,options
import textwrap

define('port',default=8088,type=int,help='run on port ')

class ReverseHandler(web.RequestHandler):
    def get(self,input):
        self.write(input[::-1])

class WrapHandler(web.RequestHandler):
    def post(self):
        text=self.get_argument('text')
        width=self.get_argument('width',40)
        self.write(textwrap.fill(text,int(width)))

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app=web.Application(handlers=[(r'/reverse/(\w+)',ReverseHandler),(r'/wrap',WrapHandler)])
    http_server=httpserver.HTTPServer(app)
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()


