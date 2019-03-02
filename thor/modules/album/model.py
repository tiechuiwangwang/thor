from datetime import datetime

from thor.exts import db
from thor.model import Base


class Photo(Base):

    __tablename__ = 'photo'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    description = db.Column(db.String(256), nullable=True)
    image_url = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True, default=None)


class PhotoLike(Base):

    __tablename__ = 'photo_like'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    photo_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           onupdate=datetime.utcnow)
    deleted_at = db.Column(db.DateTime, nullable=True, default=None)

    @classmethod
    def get_by_user_and_photo(cls, user_id, photo_id):
        return cls.query.filter_by(user_id=user_id, photo_id=photo_id).first()

    @classmethod
    def create(cls, user_id, photo_id):
        obj = cls(user_id=user_id, photo_id=photo_id)
        obj.save()
        return obj
