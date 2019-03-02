import json

from flask import Response


def json_response(data, http_status):
    return Response(data, status=http_status, mimetype="application/json")


class BusinessResponse(object):

    def __init__(self, http_code, code, error=None):
        self.http_code = http_code
        self.code = code
        self.error = error

    def __call__(self, result=None, error=None):
        return response(self, result=result, error=error)


def response(msg, result=None, error=None):
    resp = {
        'http_code': msg.http_code,
        'code': msg.code,
        'error': error or msg.error,
        'result': result,
    }
    data = json.dumps(resp)
    return json_response(data, msg.http_code)


HTTP_OK = 200
HTTP_BAD_REQUEST = 400
HTTP_FORBBIDEN = 403

ok = BusinessResponse(HTTP_OK, 0)

err_params_required = BusinessResponse(HTTP_BAD_REQUEST, 1, 'Params required')
err_params_error = BusinessResponse(HTTP_BAD_REQUEST, 2, 'Params Error')

# 1xxx for User Module
err_invalid_username_or_password = \
    BusinessResponse(HTTP_BAD_REQUEST, 1001, 'Invalid Username or Password')
