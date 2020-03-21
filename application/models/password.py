import uuid
import requests
import re
from application.common.database import Database


class Password(object):
    def __init__(self, email, _id=None):
        self.email = email
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<Item {} with URL>".format(self.email)

    def save_to_db(self):
        Database.update(PasswordConstants.COLLECTION, {'_id': self._id}, self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
        }

    @classmethod
    def get_by_id(cls, item_id):
        return cls(**Database.find_one(PasswordConstants.COLLECTION, {"_id": item_id}))