from . import db
from sqlalchemy.sql import func


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(999))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

