from flask_login import LoginManager

from thor.modules.user.model import User
from thor.utils import api


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return api.err_unauthorized_required()
