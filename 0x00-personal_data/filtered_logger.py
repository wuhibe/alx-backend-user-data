#!/usr/bin/env python3
""" module for task 0 """
import logging
import re
import typing


def filter_datum(fields: typing.List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ method to filter data """
    for f in fields:
        message = re.sub('{}=.+?{}'.format(f, separator),
                         '{}={}{}'.format(f, redaction, separator),
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        """ initialize method for class """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log records using filter_datum """
        s = filter_datum(self.fields, self.REDACTION,
                         super(RedactingFormatter, self).format(record),
                         self.SEPARATOR)
        return s
