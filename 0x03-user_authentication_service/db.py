#!/usr/bin/env python3
"""DB module
"""
from requests import session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import User, Base


class DB:
    """DB class
    """
    id = 1

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ method to add new User
        """
        usr = User(id=self.id, email=email, hashed_password=hashed_password)
        self.id += 1
        self._session.add(usr)
        self._session.commit()
        return usr

    def find_user_by(self, **kwargs) -> User:
        """ method to find User by passed arguments

        Raises:
            InvalidRequestError: if no arguments passed
            NoResultFound: if query result is none

        Returns:
            User: first match on successful query
        """
        if kwargs is None:
            raise InvalidRequestError
        users = self._session.query(User)
        u = users.filter_by(**kwargs).first()
        if not u:
            raise NoResultFound
        return u

    def update_user(self, id, **kwargs) -> None:
        """ method to update User in db

        Args:
            id (int): id to identify User

        Raises:
            ValueError: when attempted to set an attribute
            that User doesn't have
        """
        usr = self.find_user_by(id=id)
        for k, v in kwargs.items():
            if not hasattr(usr, k):
                raise ValueError
            setattr(usr, k, v)
        self._session.commit()
