from sqlalchemy import Column, ForeignKey
from sqlalchemy import (String, Integer)

from .Base import Base

class AlertCondition(Base):
    __tablename__ = 'alertCondition'
    
    id = Column(String(36), primary_key=True)
    alert_id = Column(String(36), ForeignKey('alert.id'))
    type = Column(String)
    value = Column(Integer)
