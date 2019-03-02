from flask import request
from flask_login import current_user, login_user
from flask_restful import marshal

from thor.blueprint import create_api_blueprint
from thor.utils import api

from . import schema
from .model import User
from .form import SigninForm, SignupForm


bp = create_api_blueprint('user', __name__)


@bp.route('/user/signin', methods=['POST'])
def signin_user():
    if not current_user.is_anonymous:
        return api.ok(marshal(current_user, schema.USER_FIELDS))

    if request.json is None:
        return api.err_params_required()

    form = SigninForm()
    form.validate()

    if form.errors:
        return api.err_params_error(form.errors)

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    user = User.authenticate(username, password)

    if user is None:
        return api.err_invalid_username_or_password()

    login_user(user, force=True, remember=True)

    return api.ok(marshal(current_user, schema.USER_FIELDS))


@bp.route('/user/signup', methods=['POST'])
def signup_user():
    if not current_user.is_anonymous:
        return api.ok(marshal(current_user, schema.USER_FIELDS))

    if request.json is None:
        return api.err_params_required()

    form = SignupForm()
    form.validate()

    if form.errors:
        return api.err_params_error(form.errors)

    data = form.data
    username, nickname, password = \
        data['username'], data['nickname'], data['password']

    user = User(username=username, nickname=nickname)
    user.update_password(password)

    user.save()

    return api.ok(marshal(user, schema.USER_FIELDS))
