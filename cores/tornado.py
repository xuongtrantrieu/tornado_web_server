from tornado.web import RequestHandler as RequestHandler_
from typing import Awaitable, Optional
from time import asctime


class RequestHandler(RequestHandler_):
    def prepare(self) -> Optional[Awaitable[None]]:
        method = self.request.method
        uri = self.request.uri
        current_time = asctime()
        print(f'{current_time} | {method} | {uri}')
        return
