from tornado import httpserver,ioloop,options,web
from tornado.options import define,options

define('port',default=8088,type=int,help='run on given a port')
class IndexHandler(web.RequestHandler):
    def get(self):
        greeting=self.get_argument('Greeting','Hello')
        self.write(greeting + ',new user!')

if __name__=='__main__':
    options.parse_command_line()
    app=web.Application(handlers=[(r'/',IndexHandler)])
    http_server=httpserver.HTTPServer(app)
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()

