#!/usr/bin/python3
"""
DBStorage new engine

"""

from sqlalchemy import (creat_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """New DB Engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""

        USER = os.getenv('HBNB_MYSQL_USER')
        PWD = os.getenv('HBNB_MYSQL_PWD')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        DB = os.getenv('HBNB_MYSQL_DB')
        ENV1 = os.getenv('HBNB_ENV')
        STORAGE = os.getenv('HBNB_TYPE_STORAGE')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(USER, PWD, HOST, DB),
                                      pool_pre_ping=True)

        if ENV1 == 'test':
            Base.metadata.drop_all(self.__engine)

        def all(self, cls=None):
            """public instance method ALL"""
            my_dict = {}
            if cls:
                query = self.__session.query(eval(cls))
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    my_dict[key] = obj
                else:
                    lista = [State, City, User, Place, Review, Amenity]
                    for _class in lista:
                        query = self.__session.query(_class)
                        for obj in query:
                            key = "{}.{}".format(type(obj).__name__, obj.id)
                            my_dict[key] = obj
            return my_dict

        def new(self, obj):
            """public instance method NEW"""
            if obj:
                self.__session.add(obj)

        def save(self):
            """public instance method SAVE"""
            self.__session.commit()

        def delete(self, obj=None):
            """public instance method DELETE"""
            if obj is not None:
                self.__session.delete(obj)

        def reload(self):
            """public instance method RELOAD"""
            Base.metadata.create_all(self.__engine)
            Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
            session = scoped_session(Session)
            self.__session = session()

        def close(self):
            """public instance method CLOSE"""
            self.__session.close()
