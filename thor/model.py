from datetime import datetime

from sqlalchemy import Column

from thor.exts import db


class Base(db.Model):

    __abstract__ = True

    @property
    def deleted(self):
        if hasattr(self, 'deleted_at') and self.deleted_at is not None:
            return True
        return False

    @classmethod
    def create(cls, _commit=True, **kwargs):
        obj = cls(**kwargs)
        obj.save(_commit)
        return obj

    @classmethod
    def get(cls, id_, _with_deleted=False):
        query = cls.query
        if hasattr(cls, 'deleted_at') and _with_deleted is False:
            query.filter(cls.deleted_at.is_(None))
        return query.filter_by(id=id_).first()

    def populate(self, _commit=True, **kwargs):
        for k, v in kwargs.iteritems():
            if hasattr(self, k) and isinstance(getattr(self, k), Column):
                setattr(self, k, v)
        self.save(_commit)

    def save(self, _commit=True):
        try:
            db.session.add(self)
            if _commit:
                db.session.commit()
        except Exception:
            db.session.rollback()
            raise

    def delete(self, _hard=False):
        if hasattr(self, 'deleted_at') and _hard is False:
            self.deleted_at = datetime.utcnow()
            db.session.add(self)
        else:
            db.session.delete(self)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise
