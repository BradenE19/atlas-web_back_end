#!/usr/bin/env python3
"""DB module
"""
import logging
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User

# Set SQLAlchemy log level: only show error messages and above
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)


class DB:
    """DB class
    """

    def __init__(self):
        """Initialize a new DB
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object"""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> TypeVar('User'):
        """Method saves user to DB,
        adds new user to new session,
        saves user to DB"""
        # Create user object
        user = User(email=email, hashed_password=hashed_password)
        # Add user to session
        self._session.add(user)
        # Save user to Db
        self._session.commit()
        # Return new user object
        return user
