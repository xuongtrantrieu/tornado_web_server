from tornado.web import RequestHandler
from utils import make_response, get_json, get_params


class HelloWorld(RequestHandler):
    def get(self):
        self.hello_world()

    def post(self):
        self.hello_world()

    def put(self):
        self.hello_world()

    def patch(self):
        self.hello_world()

    def hello_world(self):
        data = dict()

        arguments = get_params(self.request)
        data.update(dict(arguments=arguments))

        body_json = get_json(self.request)
        data.update(dict(body_json=body_json))

        self.write(make_response(data=data, message=f'{self.request.method} | Hello World'))
