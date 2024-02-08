#!/usr/bin/env python3
"""
Define a function that obfuscates a log
message.
"""
from typing import (
        List,
        Tuple
        )
import re
import logging
from datetime import datetime
import os
import mysql.connector


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


PII_FIELDS: Tuple[str] = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """
    Create a new logger instance with a
    custom formatter that generates logs
    to the console.

    Returns:
        A new logger instance.
    """
    logger_obj = logging.getLogger("user_data")
    logger_obj.setLevel(logging.INFO)
    logger_obj.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger_obj.addHandler(handler)

    return (logger_obj)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Establish a secure connection to a
    database.

    Returns:
        A MySQL database connection instance.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db = os.getenv("PERSONAL_DATA_DB_NAME")

    return (mysql.connector.connect(
            host=host,
            database=db,
            user=username,
            password=password)
            )
