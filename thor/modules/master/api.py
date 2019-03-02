from flask import jsonify

from thor.blueprint import create_api_blueprint


bp = create_api_blueprint('master', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return jsonify(hello='world')
