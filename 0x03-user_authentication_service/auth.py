#!/usr/bin/env python3
"""
Define a module that defines implementation
of authentication.
"""
from bcrypt import (
        hashpw,
        gensalt
        )


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
