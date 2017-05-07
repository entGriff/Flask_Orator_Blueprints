from application import db
from flask_orator import Orator
from orator.orm import belongs_to, has_many, belongs_to_many



class Message(db.Model):

    __fillable__ = ['content']

    @belongs_to
    def user(self):
        return User