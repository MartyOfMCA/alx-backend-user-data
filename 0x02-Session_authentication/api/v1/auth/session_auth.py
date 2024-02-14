#!/usr/bin/env python3
"""
Define a module that implements Session
Authentication.
"""
from .auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
    An instance of Session Authentication.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a session for the given
        user.

        Parameters:
            user_id : str, optional
            The id for a user who needs
            a new session. Default value
            ensures method fails its
            operation.

        Return:
            A uuid4 string representing the
            session created. None is
            returned should the function
            fail its operation.
        """
        if (not user_id or not isinstance(user_id, str)):
            return (None)

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return (session_id)
