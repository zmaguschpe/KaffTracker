from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(22), unique=True)
    time_reg = db.Column(db.DateTime(timezone=True), default=func.now())
    password = db.Column(db.String(999))
    infos = db.relationship('Info')
    #posts = db.relationship('Post', backref='user', passive_deletes=True)

class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(999))
    time = db.Column(db.DateTime(timezone=True), default=func.now())
    date = db.Column(db.Date(), default=func.current_date())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)

