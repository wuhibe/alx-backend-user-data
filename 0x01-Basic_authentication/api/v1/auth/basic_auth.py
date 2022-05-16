#!/usr/bin/env python3
""" Basic Authorization module
"""
import base64
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ method to decode str by base64
        """
        bah = base64_authorization_header
        if not bah or type(bah) is not str:
            return None
        try:
            bah = base64.b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            bah = None
        return bah
