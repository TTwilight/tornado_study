import os
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import random
from tornado.options import options,define

define('port',default=8088,type=int,help='input port')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class MungedHandler(tornado.web.RequestHandler):
    def map_first(self,text):
        words=text.split(' ')
        mapped={}
        for word in words:
            mapped.get(word[0],[]).append(word)
        return mapped

    def post(self):
        source_text=self.get_argument('source_text')
        change_text=self.get_argument('change_text')
        source_map=self.map_first(source_text)
        change_list=change_text.split(' ')
        new_list=[]
        for change in change_list:
            if source_map.get(change[0]):
                change=source_map.get(change[0])[random.randint(0,len(source_map.get(change[0])))]
                new_list.append(change)
            else:
                new_list.append(change)
        final_text=' '.join(new_list)
        self.render('munger.html',final_text=final_text)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app=tornado.web.Application(handlers=[
        (r'/',IndexHandler),
        (r'/munger',MungedHandler)
    ],
    template_path=os.path.join(os.path.dirname(__file__),'templates'),
    static_path=os.path.join(os.path.dirname(__file__),'static')
    )
    http_server=tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
