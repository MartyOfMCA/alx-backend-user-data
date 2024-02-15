#!/usr/bin/env python3
"""
Defines a module that implement
persisted User Session.
"""
from .base import Base


class UserSession(Base):
    """ A persisted user session. """

    def __init__(self, *args: list, **kwargs: dict):
        """ Object constructor. """
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get("user_id")
        self.session_id = kwargs.get("session_id")
