#!/usr/bin/env python3
""" Authorization module
"""
from turtle import st
from typing import TypeVar, List
from flask import request


class Auth():
    """ Authorization Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to define which routes don't need authentication
        """
        if path is None or excluded_paths is None:
            return True
        for st in excluded_paths:
            if st == path or st + '/' == path or st == path + '/':
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method to validate all requests to secure the API
        """
        if request is None:
            return None
        try:
            st = request.headers['Authorization']
        except KeyError:
            st = None
        return st

    def current_user(self, request=None) -> TypeVar('User'):
        """ Temporarily Return None """
        return None
