#!/usr/bin/env python3
"""
Defines a module that implements a Session
database Authentication.
"""
from datetime import (
        datetime,
        timedelta
        )

from .session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """
    Database for session authentication.
    """

    def create_session(self, user_id=None):
        """
        Create a session for the given
        user. Persists user session
        instance. A user session instance
        contains the session id and the
        id for the user it belongs to.

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
        session_id = super().create_session(user_id)

        if (not session_id):
            return (None)

        # Store instance of user session.
        user_session = UserSession(**{
            "user_id": user_id,
            "session_id": session_id
            })
        self.user_id_by_session_id[session_id] = user_session
        user_session.save()

        return (session_id)

    def user_id_for_session_id(self, session_id=None):
        """
        Retrieve the id for the user who
        owns the session with the given
        id.

        Parameters:
            session_id  : str, optional
            The id for the session whose
            user has to be retrieved. Default
            value ensures method fails its
            operation.

        Return:
            The id for the user with the
            given session. None is returned
            should the function fail its
            operation.
        """
        # Abort operation if session_id is
        # not valid
        if (not session_id or not isinstance(session_id, str)):
            return (None)

        # Abort operation if given session is
        # not a valid session found in the
        # stored sessions.
        if (session_id not in self.user_id_by_session_id):
            return (None)

        # Fetch the user session's instance
        user_session = self.user_id_by_session_id[session_id]

        # Fetch the expiry date of the user's
        # current session.
        session_expiry = user_session.created_at +\
            timedelta(seconds=self.session_duration)

        # Abort operation if the user's
        # session is expired.
        if ((session_expiry - datetime.now()).total_seconds() < 0):
            # Delete user session instance
            user_session.remove()
            del self.user_id_by_session_id[session_id]
            return (None)

        return (user_session.user_id)

    def destroy_session(self, request=None):
        """
        Invalide the current session for the
        given request.

        Parameters:
            request : LocalProxy
            A Flask request object to process.

        Return:
            A boolean indicating whether the
            session is destroyed or nt.
        """
        if (not request):
            return (False)

        # Return false flag when the request
        # has no cookie (or the value None).
        session_id = self.session_cookie(request)
        if (not session_id):
            return (False)

        # Return false flag when session for
        # some reason is not for the current
        # user.
        if (not self.user_id_for_session_id(session_id)):
            return (False)

        # Delete user's session.
        self.user_id_by_session_id[session_id].remove()
        del self.user_id_by_session_id[session_id]

        return (True)
