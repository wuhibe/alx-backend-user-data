#!/usr/bin/env python3
""" module for task 0 """
import re


def filter_datum(fields, redaction, message, separator):
    """ method to filter data """
    for f in fields:
        message = re.sub('{}=.+?{}'.format(f, separator),
                         '{}={}{}'.format(f, redaction, separator),
                         message)
    return message
