from sqlalchemy import Column, String, Integer, ForeignKey

from .Base import Base

class Sensor(Base):
    __tablename__ = 'sensor'
    
    id = Column(String(36), primary_key=True)
    name = Column(String)
    type = Column(String)
    device_id = Column(String(36), ForeignKey('device.id'))
    
    def __repr__(self):
        repr_str = f"""Sensor(
            id={self.id!r}, 
            name={self.name!r}, 
            type={self.type!r}, 
            device_id={self.device_id!r}
        )"""
        return repr_str
