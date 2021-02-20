"""All Generic CRUD actions"""
from app.models import db
from .log_handle import log_file_handle


class CrudAction:
    def __init__(self, models):
        self.models = models

    def create(self, fields):
        try:
            record = self.models(**fields)
            db.session.add(record)
            db.session.commit()
            log_file_handle(" CrudAction(Create) SUCCESS: " + str(record))
        except Exception as ex:
            log_file_handle(" CrudAction(Create) ERROR: " + str(ex))

    def read(self, custom_filter=None):
        try:
            if custom_filter:
                record = db.session.query(self.models).filter_by(**custom_filter)
            else:
                record = self.models.query.all()
            return record
        except Exception as ex:
            log_file_handle(" CrudAction(Read) ERROR: " + str(ex))

    def update(self):
        try:
            pass
        except Exception as ex:
            log_file_handle(" CrudAction(Update) ERROR: " + str(ex))

    def delete(self):
        try:
            pass
        except Exception as ex:
            log_file_handle(" CrudAction(Delete) ERROR: " + str(ex))
