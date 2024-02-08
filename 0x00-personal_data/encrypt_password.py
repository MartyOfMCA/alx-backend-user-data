#!/usr/bin/env python3
"""
Define a function to hash user password.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash the given password.

    Parameters:
        password : str
        The password that needs to be
        hashed.

    Returns:
        A salted hashed password.
    """
    return (bcrypt.hashpw(bytes(password, "utf-8"), bcrypt.gensalt(14)))
