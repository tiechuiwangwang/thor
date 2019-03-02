from envcfg.json import thor as config
from flask import Flask
from werkzeug.utils import import_string

from thor.exts import db, login_manager


blueprints = [
    'thor.modules.album.api:bp',
    'thor.modules.master.api:bp',
    'thor.modules.user.api:bp',
]


def create_app(import_name=None):
    app = Flask(import_name or __name__)

    app.config.from_object('envcfg.json.thor')
    app.debug = bool(int(config.DEBUG))

    db.init_app(app)
    login_manager.init_app(app)

    for bp_import_name in blueprints:
        bp = import_string(bp_import_name)
        app.register_blueprint(bp)

    return app
