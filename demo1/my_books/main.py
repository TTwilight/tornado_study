import tornado.web
import tornado.httpserver
import tornado.options
import tornado.ioloop
import os.path
from tornado.options import options,define

define('port',default=8088,type=int,help='input port')

class Application(tornado.web.Application):
    def __init__(self):
        handlers=[
            (r'/',IndexHandler),
            (r'/recommand',RecommandHandler),
        ]
        settings=dict(
            static_path=os.path.join(os.path.dirname(__file__),'static'),
            template_path=os.path.join(os.path.dirname(__file__),'templates'),
            debug=True,
            ui_modules={'Book': BookModule}
        )
        tornado.web.Application.__init__(self,handlers,**settings)

class BookModule(tornado.web.UIModule):
    def render(self,book):
        return self.render_string('modules/book.html',book=book)
    #add css,js sentence
    def embedded_javascript(self):
        return 'document.write(\"hi\")'
    def embedded_css(self):
        return '.book{background-color:blue }'
    # add css , js files
    def css_files(self):
        return "https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap-theme.min.css"
    def javascript_files(self):
        return "https://cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js"

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html',page_title='my books | home',header_text='welcome to my books center')

class RecommandHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("recommended.html",
            page_title="Burt's Books | Recommended Reading",
            header_text="Recommended Reading",
            books=[
                {
                    "title":"Programming Collective Intelligence",
                    "subtitle": "Building Smart Web 2.0 Applications",
                    "image":"images/webwxgetmsgimg.jpg",
                    "author": "Toby Segaran",
                    "date_added":1310248056,
                    "date_released": "August 2007",
                    "isbn":"978-0-596-52932-1",
                    "description":"<p>This fascinating book demonstrates how you "
                        "can build web applications to mine the enormous amount of data created by people "
                        "on the Internet. With the sophisticated algorithms in this book, you can write "
                        "smart programs to access interesting datasets from other web sites, collect data "
                        "from users of your own applications, and analyze and understand the data once "
                        "you've found it.</p>"
                },])

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()