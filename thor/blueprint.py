from flask import Blueprint


def create_api_blueprint(name, package_name, **kwargs):
    blueprint_name = name
    return _create_bp(blueprint_name, package_name, **kwargs)


def _create_bp(name, package_name, **kwargs):
    bp = Blueprint(
        name, package_name,
        **kwargs)

    return bp
