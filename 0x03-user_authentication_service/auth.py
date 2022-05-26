#!/usr/bin/env python3
""" module for auth
"""
import bcrypt


def _hash_password(password) -> str:
    salt = bcrypt.gensalt()
    password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return password
