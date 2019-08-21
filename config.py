from os import getenv as get_env
from dotenv import load_dotenv
from tornado.web import Application

load_dotenv()

APP = Application()


def load_app():
    from handlers import (
        HelloWorldHandler,
        MessageHandler, MessageNewHandler, MessageUpdateHandler,
    )

    APP.listen(8000)
    APP.add_handlers(r'www\.xuong\.com', [
        (r'/', HelloWorldHandler),
        (r'/message', MessageHandler),
        (r'/message/new', MessageNewHandler),
        (r'/message/update', MessageUpdateHandler),
    ])
