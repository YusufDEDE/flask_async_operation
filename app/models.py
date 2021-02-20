from . import db


class Task(db.Model):
    __tablename__ = "flask_async_operation"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=False, unique=False, nullable=False)
    priority = db.Column(db.String(80), index=True, unique=False, nullable=False)
    status = db.Column(db.String(80), index=True, unique=False, nullable=False)
    created = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    def __repr__(self):
        return "<Task {}>".format(self.name)
