#!/usr/bin/python3
""" BaseModel SQLAlchemy"""
# models/base_model.py
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import models

Base = declarative_base()


class BaseModel:
    """ Attributes and Methods of the BaseModel """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def save(self):
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)

    def to_dict(self):
        data = dict(self.__dict__)
        data.pop('_sa_instance_state', None)
        return data
