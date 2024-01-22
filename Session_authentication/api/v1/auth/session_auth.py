#!/usr/bin/env python3
"""Session authorization method"""

from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64
import uuid
from models.user import User


class SessionAuth(Auth):
    """Session Auth class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creat session for auth"""
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a user id based on session id"""
        if session_id and isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        """current user id"""
        session_cookie = self.session_cookie(request)
        session_id = self.user_id_for_session_id(session_cookie)
        return User.get(session_id)

    def destroy_session(self, request=None):
        """session teardown"""
        if not request:
            return False
        session_cookie = self.session_cookie(request)

        if not session_cookie:
            return False

        user_id = self.user_id_for_session_id(session_cookie)

        if not user_id:
            return False
        self.user_id_by_session_id.pop(session_cookie)
        return True
