#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            from models import storage
            from models.city import City
            objs = []
            cities = storage.all(City)
            for key, value in cities.items():
                if self.id == value.state_id:
                    objs.append(value)
            return objs
    else:
        cities = relationship("City", backref="state", cascade="all, delete")
