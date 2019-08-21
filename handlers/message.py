from tornado.locks import Condition
from tornado.web import RequestHandler
from tornado.iostream import BaseIOStream
from uuid import uuid4 as make_id
from typing import List, Awaitable, Union
from asyncio import CancelledError
from utils import make_response


class MessageBuffer:
    def __init__(self):
        self.condition = Condition()
        self.cache: List[dict] = []
        self.cache_size = 200

    def get_message_since(self, cursor):
        result: List[dict] = []
        for message in reversed(self.cache):
            id_ = message['id']
            if id_ == cursor:
                break

            result.append(message)

        result.reverse()

        return result

    def add_message(self, message):
        self.cache.append(message)
        if len(self.cache) > self.cache_size:
            self.cache = self.cache[-self.cache_size:]


GLOBAL_MESSAGE_BUFFER = MessageBuffer()


class MessageHandler(RequestHandler):
    def get(self):
        self.write(make_response(message='Welcome to message handler'))


class MessageNewHandler(RequestHandler):
    def post(self):
        message = dict(
            id=make_id(),
            body=self.get_argument('body') or ''
        )
        GLOBAL_MESSAGE_BUFFER.add_message(message)
        self.write(message)


class MessageUpdateHandler(RequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.waiting_futures: Union[None, Awaitable] = None

    async def post(self):
        cursor = self.get_argument('cursor') or ''
        messages = GLOBAL_MESSAGE_BUFFER.get_message_since(cursor)
        while not messages:
            self.waiting_futures = GLOBAL_MESSAGE_BUFFER.condition.wait()
            try:
                await self.waiting_futures
            except CancelledError:
                return

        stream: Union[None, BaseIOStream] = self.request.connection.stream
        if stream.closed():
            return

        self.write(make_response(data=messages))

    def on_connection_close(self):
        self.waiting_futures.cancel()
