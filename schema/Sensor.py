from sqlalchemy import Column, ForeignKey
from sqlalchemy import (String, Integer)

from .Base import Base

class Sensor(Base):
    __tablename__ = 'sensor'
    
    id = Column(String(36), primary_key=True)
    name = Column(String)
    type = Column(String)
    device_id = Column(String(36), ForeignKey('device.id'))
