import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
from tornado.options import options,define
import pymongo
import os,time
define('port',default=8088,type=int,help='input port')

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[(r'/(\w+)',IndexHandler),(r'/',WordHandler)]
        settings=dict(
            template_path=os.path.join(os.path.dirname(__file__),'templates'),
            Debug=True,
        )
        conn=pymongo.MongoClient('localhost',27017)
        self.db=conn['web_dict']
        tornado.web.Application.__init__(self,handlers,**settings)


class IndexHandler(tornado.web.RequestHandler):
    def get(self,word):

        coll=self.application.db.example
        word_doc=coll.find_one({'word':word})
        if word_doc:
            del word_doc['_id']
            self.write(word_doc)
        else:
            self.set_status(404)
            self.write({'error':'can not find this word'})
            # time.sleep(0.5)
            # self.redirect('/add')
class WordHandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('add.html')
    def post(self):
        word=self.get_argument('word')
        definition=self.get_argument('definition')
        word_doc = {'word': str(word), 'definition': str(definition)}
        self.write(word_doc)
        coll=self.application.db.example
        if word and definition:
            word_doc={'word':word,'definition':definition}
            coll.insert(word_doc)
            self.write('add success ! ')
        else:
            self.write({'error':'incorrect value'})

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

