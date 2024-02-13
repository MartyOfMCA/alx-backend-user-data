#!/usr/bin/env python3
"""
Module that defines a class for
Authentication.
"""
from flask import request
from typing import (
        List,
        TypeVar
        )
from re import search


class Auth:
    """
    An instance of authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether authentication is
        required for the given path. A path
        denotes an endpoint to a route.

        Arguments:
            path : str
            The path to validate.

            excluded_paths : List
            A list of paths excluded.

        Returns:
            A boolean indicating whether the
            given path requires authentication
            or not.
        """
        is_excluded_path = True

        if (path is None or excluded_paths in ["", None]):
            return (True)

        # Make sure given path is well-formed
        if (path[-1] != '/'):
            path += '/'

        for excluded_path in excluded_paths:
            #if (path == excluded_path):
            if (search(excluded_path, path)):
                is_excluded_path = False
                break

        return (is_excluded_path)

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authoriztion header
        for the given request.

        Parameters:
            request : LocalProxy
            A Flask request object to process.

        Returns:
            A string bearing the authorization
            found in the request header
            otherwise None.
        """
        if (request is None):
            return (None)

        headers = request.headers

        return (headers.get("Authorization"))

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Obtain an instance for the current
        user.

        Parameters:
            request : LocalProxy
            A Flask request object to procss.

        Returns:
            An instance for the active user
            otherwise None.
        """
        return (None)
