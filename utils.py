from tornado.escape import json_decode
from tornado.httputil import HTTPServerRequest
from typing import List


def make_response(data=[], message: str = '', errors: List[dict] = []):
    if not isinstance(data, list):
        data = [data]

    return dict(
        data=data,
        message=message,
        errors=errors,
    )


def get_json(request: HTTPServerRequest):
    return json_decode(request.body)


def get_params(request: HTTPServerRequest):
    arguments = dict()
    for key, value in request.arguments.items():
        try:
            arguments.update({key: [x.decode('utf-8') for x in value]})
        except ValueError:
            continue

    return arguments
