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
HTTP_UNAUTHORIZED = 401
HTTP_FORBBIDEN = 403
HTTP_NOT_FOUND = 404

ok = BusinessResponse(HTTP_OK, 0)

err_unauthorized_required = \
    BusinessResponse(HTTP_UNAUTHORIZED, 1, 'Login required')

err_params_required = BusinessResponse(HTTP_BAD_REQUEST, 2, 'Params required')

err_params_error = BusinessResponse(HTTP_BAD_REQUEST, 3, 'Params Error')

err_unkown = BusinessResponse(HTTP_BAD_REQUEST, 9, 'Unkown Error')

# 1xxx for User module
err_invalid_username_or_password = \
    BusinessResponse(HTTP_BAD_REQUEST, 1001, 'Invalid Username or Password')
err_user_is_inactive = \
    BusinessResponse(HTTP_BAD_REQUEST, 1002, 'Inactive User')
err_username_exists = \
    BusinessResponse(HTTP_BAD_REQUEST, 1003, 'Username Exists')

# 2xxx for Album module
err_photo_not_found = \
    BusinessResponse(HTTP_NOT_FOUND, 2001, 'Photo Not Found')
err_photo_already_liked = \
    BusinessResponse(HTTP_BAD_REQUEST, 2002, 'You Have Liked the Photo')
