from sqlalchemy import Column, Integer, String, Boolean, Float
from connection import Base


class Website(Base):
    __tablename__ = 'website'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    website = Column(String)
    descr = Column(String)
    ads = Column(String)
    ssl = Column(Boolean)
    points = Column(Float)
    multilang = Column(String)
