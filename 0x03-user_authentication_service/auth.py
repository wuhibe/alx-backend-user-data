#!/usr/bin/env python3
""" module for auth
"""
import uuid
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """ method to generate a hashed password
        from a given string
    """
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password.encode(), salt)
    return password


def _generate_uuid() -> str:
    """method to generate id
    """
    id = uuid.uuid4()
    return str(id)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ method to register User
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            hashed = _hash_password(password)
            usr = self._db.add_user(email, hashed)
            return usr

    def valid_login(self, email: str, password: str) -> bool:
        """ method to check if a login is valid
        """
        try:
            usr = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode(), usr.hashed_password):
                return True
        except Exception:
            pass
        return False
