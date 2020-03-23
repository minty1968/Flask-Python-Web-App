import uuid
from flask import session, flash
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return '<User {}>'.format(self.email)

    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)

    @staticmethod
    def login_valid(email, password):
        """
        This method verifies that an e-mail/password combo (as sent by the site forms) is valid or not.
        Checks that the e-mail exists, and that the password associated to that e-mail is correct.
        """
        user_data = Database.find_one("users", {"email": email})  # Password in sha512 -> pbkdf2_sha512
        print(user_data)
        if user_data is None:
            # Tell the user that their e-mail doesn't exist
            flash("Your user does not exist.")
        if not Utils.check_hashed_password(password, user_data['password']):
            # Tell the user that their password is wrong
            flash("Your password was wrong.")
        return True

    @staticmethod
    def signup_user(email, password):
        """
        This method registers a user using e-mail and password.
        The password already comes hashed as sha-512.
        """
        flash("I'm in the registration function")
        user_data = Database.find_one("users", {"email": email})
        if user_data is not None:
            flash('A user already exists with that email address.')
        if not Utils.email_is_valid(email):
            flash("The e-mail does not have the right format.")
        User(email, Utils.hash_password(password)).save_to_db()
        return True

    @staticmethod
    def login_user(user_email):
        # login_valid has already been called
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def json(self):
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.password
        }

    def save_to_db(self):
        Database.insert("users", self.json())
