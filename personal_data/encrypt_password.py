#!/usr/bin/env python3
"""implementing a hash password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """takes one string and returns as hash password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
    """takes in 2 args and returns a boolean to match passwords"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
