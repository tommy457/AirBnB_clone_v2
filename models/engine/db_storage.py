#!/usr/bin/python3
""" State Module for DBStorage engine"""
from sqlalchemy import create_engine
from models.base_model import Base
import os
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """This class manages storage of hbnb models in MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get("HBNB_MYSQL_USER"),
            os.environ.get("HBNB_MYSQL_PWD"),
            os.environ.get("HBNB_MYSQL_HOST", default="localhost"),
            os.environ.get("HBNB_MYSQL_DB")), pool_pre_ping=True)

        if os.environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of objects of one type of cls"""
        results_dict = {}

        if cls:

            results = self.__session.query(cls).all()
            for obj in results:
                results_dict[{cls.__name__} + '.' + {obj.id}] = obj
        else:
            cls = [State, City, User, Place, Review, Amenity]
            for c in cls:
                results = self.__session.query(c).all()

                for obj in results:
                    results_dict[f"{type(obj).__name__}.{obj.id}"] = obj

        return results_dict

    def new(self, obj):
        """Adds new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an object from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the session in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """call remove on the private session attribute self.__session"""
        self.__session.close()
