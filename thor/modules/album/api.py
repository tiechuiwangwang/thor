from flask import jsonify, request

from thor.consts import DEFAULT_PAGE, DEFAULT_PER_PAGE
from thor.blueprint import create_api_blueprint
from thor.modules.album.model import Photo


bp = create_api_blueprint('album', __name__)


@bp.route('/album/photo.list')
def photo_list():
    page = request.args.get('page', default=DEFAULT_PAGE, type=int)
    per_page = request.args.get('per_page', default=DEFAULT_PER_PAGE, type=int)
    photos = Photo.query.order_by(Photo.id.desc()).paginate(page=page,
                                                            per_page=per_page,
                                                            error_out=False)
    return jsonify(data=photos.items)
