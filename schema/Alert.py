from sqlalchemy import Column, ForeignKey
from sqlalchemy import (String, Integer)

from .Base import Base

class Alert(Base):
    __tablename__ = 'alert'
    
    id = Column(String(36), primary_key=True)
    name = Column(String)
    sensor_id = Column(String(36), ForeignKey('sensor.id'))
    status = Column(String)
    status_timestamp = Column(Integer)
