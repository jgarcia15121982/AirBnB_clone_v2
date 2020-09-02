#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref='state')

    @property
    def cities(self):
        """method that return the cities"""

        dict_2 = models.storage.all(City)
        list_2 = []
        for res1 in dict_2.values():
            if res1.state_id == self.id:
                list_2.append(res1)
        return list_2
