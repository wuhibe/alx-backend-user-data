#!/usr/bin/env python3
""" Basic Authorization module
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Authorization Class
    Inheriting from Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str
                                            ) -> str:
        """ method to find base64 string in header
        """
        if not authorization_header or type(authorization_header) is not str:
            return None
        lst = authorization_header.split(" ")
        if lst[0] == 'Basic':
            lst.pop(0)
            return ' '.join(lst)
        return None
