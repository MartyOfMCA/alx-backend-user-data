#!/usr/bin/env python3
"""
Define a function that obfuscates a log
message.
"""
from typing import List
import re
import logging
from datetime import datetime


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class. """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Object constructor.

        Parameters:
            fields : list
            A list of string containing the
            fields to obfuscate.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self._fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the message displayed in the log.

        Parameters:
            record : Log Record
            The records of the log.

        Returns:
            A string
        """
        record.msg = filter_datum(self._fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return (super().format(record))


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
