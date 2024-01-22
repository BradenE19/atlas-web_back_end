#!/usr/bin/env python3
"""session authentication method"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


