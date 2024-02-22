#!/usr/bin/env python3
"""
Define a module that defines implementation
of authentication.
"""
from bcrypt import (
        hashpw,
        gensalt
        )
from sqlalchemy.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    Returns an excypted and salted
    password.

    Parameters:
        password : str
        The password to be encrypted.

    Return:
        Salted hash of the password
        given.
    """
    return (hashpw(bytes(password, "utf-8"), gensalt(14)))


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email, password) -> User:
        """
        Add a new user wih the given
        credentials.

        Parameters:
            email : str
            The email of the new user.

            password : str
            The password of the new user.

        Return:
            The new user instance created.
        """
        try:
            # Find existing user with the given
            # email to abort operation.
            user = self._db.find_user_by(**{"email": email})
            print(f"User {email} already exists")
        except NoResultFound:
            return (self._db.add_user(email, _hash_password(password)))
