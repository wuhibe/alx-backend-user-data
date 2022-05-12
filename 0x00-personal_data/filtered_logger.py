#!/usr/bin/env python3
""" module for task 0 """
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
