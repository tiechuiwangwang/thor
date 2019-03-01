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
