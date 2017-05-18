import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import options,define

define('port',default=8088,type=int,help='input port')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        cookie=self.get_secure_cookie('count')
        print cookie
        count= int(cookie)+1 if cookie else 1
        countString= '1 time' if count==1 else '%s times' % count
        self.set_cookie('count',str(count))
        self.write(
             countString 
        )
if __name__ == '__main__':
    tornado.options.parse_command_line()
    settings={
        'cookie_secret' : 'bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E='
    }
    application=tornado.web.Application(
        handlers=[
            (r'/',MainHandler)
        ],
        **settings
    )
    http_server=tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
