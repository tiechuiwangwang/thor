from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from thor.exts import db
from thor.model import Base


class User(Base):

    __tablename__ = 'user'

    STATUS_PENDING = 0
    STATUS_NORMAL = 1

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))
    nickname = db.Column(db.String(64), nullable=True)
    avatar = db.Column(db.String(256))
    status = db.Column(db.Integer, default=STATUS_PENDING)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True, default=None)

    def __init__(self, **kwargs):
        password = kwargs.get('password', None)
        if password is not None:
            self.update_password(password)
        return super(User, self).__init__(**kwargs)

    def update_password(self, raw_password):
        self.password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def authenticate(cls, username, raw_password):
        user = cls.query.filter_by(username=username).first()
        if user is not None and user.check_password(raw_password):
            return user
        return None

    def get_id(self):
        return self.id

    def is_active(self):
        return self.status == User.STATUS_NORMAL

    def is_anonymous(self):
        return (self.username is None)

    def is_authenticated(self):
        return (self.username is not None)
