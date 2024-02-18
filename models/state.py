#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if models.storage_t == 'db':
        cities = relationship(
                "City",
                backref="state",
                cascade="all,
                delete-orphan"
                )

    else:
        @property
        def cities(self):
            """
            Getter method to return the list of
            City objects linked to the current State
            """
            cities_list = []
            for city_obj in list(models.storage.all(City).values()):
                if city_obj.state_id == self.id:
                    cities_list.append(city_obj)
            return cities_list
