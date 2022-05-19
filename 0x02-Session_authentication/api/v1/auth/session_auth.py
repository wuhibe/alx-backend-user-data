#!/usr/bin/env python3
""" Session Authorization module
"""
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Basic Authorization Class
    Inheriting from Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ instance method to create a session
        """
        if not user_id or type(user_id) is not str:
            return None
        sess_id = str(uuid.uuid4())
        self.user_id_by_session_id[sess_id] = user_id
        return sess_id
