#!/usr/bin/env python3
"""session authentication method"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


class SessionAuth(Auth):
    """SessionAuth"""
    user_id_by_session_id = {}