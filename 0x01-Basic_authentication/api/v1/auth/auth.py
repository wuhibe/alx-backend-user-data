#!/usr/bin/env python3
""" Authorization module
"""
from typing import TypeVar, List
from flask import request


class Auth():
    """ Authorization Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Temporarily return False """
        return False

    def authorization_header(self, request=None) -> str:
        """ Temporarily return None """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Temporarily Return None """
        return None
