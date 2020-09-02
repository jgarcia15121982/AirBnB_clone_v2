#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String
import models
from os import environ
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ.get('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City", cascade="all, delete, delete-orphan",
                              backref='state')
    else:
        @property
        def cities(self):
            """method that return the cities"""
            dict_2 = models.storage.all(City)
            list_2 = []
            for res1 in dict_2.values():
                if res1.state_id == self.id:
                    list_2.append(res1)
            return list_2
