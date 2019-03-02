from flask import request
from flask_restful import marshal
from flask_login import login_required, current_user

from thor.consts import DEFAULT_PAGE, DEFAULT_PER_PAGE
from thor.blueprint import create_api_blueprint
from thor.utils import api

from . import schema
from .model import Photo, PhotoLike


bp = create_api_blueprint('album', __name__)


@bp.route('/album/photo.list')
def photo_list():
    page = request.args.get('page', default=DEFAULT_PAGE, type=int)
    per_page = request.args.get('per_page', default=DEFAULT_PER_PAGE, type=int)
    photos = Photo.query.order_by(Photo.id.desc()).paginate(page=page,
                                                            per_page=per_page,
                                                            error_out=False)
    return api.ok(marshal(photos.items, schema.PHOTO))


@bp.route('/album/photo.like', methods=['POST'])
@login_required
def photo_like():
    if request.json is None:
        return api.err_params_required()

    photo_id = request.json.get('photo_id', type=int)

    if photo_id is None:
        return api.err_params_error('Photo id cannot be Empty')

    photo = Photo.query.get(photo_id)

    if photo is None:
        return api.err_photo_not_found()

    user_id = current_user.id
    found_pl = PhotoLike.get_by_user_and_photo(user_id, photo.id)
    if found_pl is not None:
        return api.err_photo_already_liked()

    pl = PhotoLike.create(user_id=user_id, photo_id=photo.id)

    if pl is None:
        return api.err_unkown()
    else:
        return api.ok()
