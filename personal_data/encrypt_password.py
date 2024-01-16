#!/usr/bin/env python3
"""implementing a hash password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """takes one string and returns as hash password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
