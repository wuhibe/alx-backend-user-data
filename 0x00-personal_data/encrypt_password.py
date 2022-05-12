#!/usr/bin/env python3
""" module for tasks 5 and 6 """
import bcrypt


def hash_password(password: str) -> bytes:
    """ method to convert plain text password to hash """
    encoded = password.encode()
    return bcrypt.hashpw(encoded, bcrypt.gensalt())
