from tornado.ioloop import IOLoop
from config import load_app

if __name__ == '__main__':
    load_app()
    main_loop = IOLoop.current()
    try:
        main_loop.start()
    except KeyboardInterrupt:
        main_loop.stop()
