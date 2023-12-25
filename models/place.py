#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                      Column(
                          'place_id', String(60),
                          ForeignKey("places.id"),
                          primary_key=True,
                          nullable=False
                          ),
                      Column(
                          'amenity_id',
                          String(60),
                          ForeignKey("amenities.id"),
                          primary_key=True,
                          nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place")
        amenities = relationship(
            "Amenity",
            back_populates="place_amenities",
            secondary=place_amenity,
            viewonly=False
            )

    else:
        @property
        def reviews(self):
            from models import storage
            from models.review import Review
            objs = []
            reviews = storage.all(Review)
            for value in reviews:
                if self.id == value.place_id:
                    objs.append(value)
            return objs

        @property
        def amenities(self):
            from models import storage
            from models.amenity import Amenity
            objs = []
            amenities = storage.all(Amenity)
            for value in amenities:
                if self.id == value.place_id:
                    objs.append(value)
            return objs

        @amenities.setter
        def amenities(self, obj):
            from models import storage
            from models.amenity import Amenity

            if isinstance(obj, storage.all(Amenity)):
                self.amenity_ids.append(obj.id)
