from tornado.ioloop import IOLoop
from config import load_app

if __name__ == '__main__':
    load_app()
    IOLoop.current().start()
