#!/usr/bin/env python3
"""
Define a function that obfuscates a log
message.
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates the given message.

    Parameters:
        fields : list
        The list of fields in the message to
        obfuscate.

        redaction : str
        The string used as replacement when
        obfuscating the message.

        message : str
        The gven message.

        separator : str
        The character used to separate tokens
        in the message.

    Returns:
        An obfuscated message.
    """
    for field in fields:
        message = re.sub(f"{field}=.+?{separator}",
                         f"{field}={redaction}{separator}",
                         message)
    return (message)
