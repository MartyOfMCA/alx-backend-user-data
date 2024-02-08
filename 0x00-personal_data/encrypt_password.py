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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks whether the given password is
    the same as the hashed pasword.

    Parameters:
        hashed_password : bytes
        A salted and hashed password.

        password : str
        The given password to validate.

    Returns:
        True when both `hashed_password` and
        `password` are the same otherwise
        False.
    """
    return (bcrypt.checkpw(bytes(password, "utf-8"), hashed_password))
