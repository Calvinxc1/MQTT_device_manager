from sqlalchemy import Column
from sqlalchemy import (String, Integer)

from .Base import Base

class Device(Base):
    __tablename__ = 'device'
    
    id = Column(String(36), primary_key=True)
    name = Column(String)
    location = Column(String)
    status = Column(String)
    status_timestamp = Column(Integer)
    
    def __repr__(self):
        return self._repr(
            id=self.id,
            name=self.name,
            location=self.location,
            status=self.status,
            status_timestamp=self.status_timestamp,
        )
