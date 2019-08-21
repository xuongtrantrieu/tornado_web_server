from tornado.ioloop import IOLoop
from config import load_app

if __name__ == '__main__':
    print('Starting server...')
    load_app()
    main_loop = IOLoop.current()
    try:
        def notice_start():
            print('Server started!')
        main_loop.spawn_callback(notice_start)
        main_loop.start()
    except KeyboardInterrupt:
        print('\nServer stopped!')
        main_loop.stop()
