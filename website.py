from sqlalchemy import Column, Integer, String, Float
from connection import Base


class Website(Base):
    __tablename__ = 'website'
    id = Column(Integer, primary_key=True)
    url = Column(String)
    title = Column(String)
    html_version = Column(Float)
    description = Column(String)
    #domain = Column(String)
    #pages_count = Column(Integer)
