#!/usr/bin/env python3
"""
Define a module that provides the DB
instance for SQLite database maniulations.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import (
        Base,
        User
        )


class DB:
    """DB class
    """

    def __init__(self):
        """
        Object constructor.
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """ Database session property. """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user instance to the
        underlying database.

        Parameters:
            email : str
            The email for the user.

            hashed_password : str
            The password of the user
            as a hashed string.

        Return:
            The user instance stored in
            the underlying database.
        """
        user = User(
                email=email,
                hashed_password=hashed_password
                )
        self._session.add(user)
        self._session.commit()

        return (user)
