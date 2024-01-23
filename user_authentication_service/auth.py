#!/usr/bin/env python3
""" Authentication Module """

from db import DB
from user import User
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the input password """
    return hashpw(password.encode('utf-8'), gensalt())
